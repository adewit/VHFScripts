import ROOT
from pprint import pprint
import CombineHarvester.CombineTools.plotting as plot
#from Acorn.Analysis.analysis import *
from array import array
import argparse
import math
import json
import sys
import os
import fnmatch

ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.TH1.AddDirectory(False)

plot.ModTDRStyle()

def createAxisHists(n,src,xmin=0,xmax=499):
  result = []
  for i in range(0,n):
    res = src.Clone()
    res.Reset()
    res.SetTitle("")
    res.SetName("axis%(i)d"%vars())
    res.SetAxisRange(xmin,xmax)
    res.SetStats(0)
    result.append(res)
  return result

parser= argparse.ArgumentParser()
parser.add_argument('--variable',default='nAddJets',help='Variable to plot')
parser.add_argument('--nbins',default='20',help='Number of bins')
parser.add_argument('--xmin',default='0',help='X axis minimum')
parser.add_argument('--xmax',default='200',help='X axis maximum')
parser.add_argument('--selection',default='(V_pt>150&&nAddJets<2)',help='Selection to apply')
parser.add_argument('--weights', default='intWeight', help='Weight to apply')
#including all weights is intWeight*WJetNLOWeight*recoWReWeight*weight_ptEWK
parser.add_argument('--outnextra',default='',help='Additional string for output name')
parser.add_argument('--xlabel',default='nAddJets',help='x-axis label')
parser.add_argument('--uncerts',default=None,help='Uncertainties to apply')
#Can have: nlo,wrew,scale

args=parser.parse_args()
nbins = int(args.nbins)
xmin = float(args.xmin)
xmax = float(args.xmax)

wt_up="1"
wt_down="1"

doUncerts=False

if args.uncerts is not None:
    doUncerts=True
    if 'nlo' in args.uncerts:
        wt_up+="*WJetNLOWeight"
        wt_down+="*(1/WJetNLOWeight)"
    if 'wrew' in args.uncerts:
        wt_up+="*(recoWReWeightUp/recoWReWeight)"
        wt_down+="*(recoWReWeightDown/recoWReWeight)"
    if 'scale' in args.uncerts:
        wt_up+="*LHE_weights_scale_muRmuFUp"
        wt_down+="*LHE_weights_scale_muRmuFDown"



inputfiles = ["sum_WJets-HT100To200_0.root","sum_WJets-HT100To200_1.root","sum_WJets-HT100To200_1.root","sum_WJets-HT1200To2500_0.root","sum_WJets-HT200To400_0.root","sum_WJets-HT200To400_1.root","sum_WJets-HT400To600_0.root","sum_WJets-HT600To800_0.root","sum_WJets-HT800To1200_0.root","sum_WJets-HT800To1200_1.root","sum_WJets_madgraph_0.root","sum_WJets_madgraph_1.root"]

histo_nominal = ROOT.TH1F("histo_nominal","histo_nominal",nbins,xmin,xmax)
histo_nominal.Sumw2()
histo_nominal.SetMarkerSize(0)

histo_unc_up = ROOT.TH1F("histo_unc_up","histo_unc_up",nbins,xmin,xmax)
histo_unc_up.Sumw2()
histo_unc_up.SetLineColor(ROOT.kRed)
histo_unc_up.SetLineWidth(2)
histo_unc_up.SetMarkerSize(0)

histo_unc_down = ROOT.TH1F("histo_unc_down","histo_unc_down",nbins,xmin,xmax)
histo_unc_down.Sumw2()
histo_unc_down.SetLineColor(ROOT.kRed)
histo_unc_down.SetLineWidth(2)
histo_unc_down.SetMarkerSize(0)


for fname in inputfiles:
  filein = ROOT.TFile.Open("/nfs/dust/cms/user/dewita/VHbbGenAnalysisNtuples/VHbbGen_0307_wjets_bHadMatch_jetfilter/haddjobs/%s"%fname)
  tree = filein.Get("Events")

  histo_nominal.SetDirectory(ROOT.gDirectory)
  histo_unc_up.SetDirectory(ROOT.gDirectory)
  histo_unc_down.SetDirectory(ROOT.gDirectory)

  tree.Draw("%s>>+histo_nominal"%args.variable,"%s*%s"%(args.selection,args.weights))
  if doUncerts:
      tree.Draw("%s>>+histo_unc_up"%args.variable,"%s*%s"%(args.selection,args.weights+"*"+wt_up))
      tree.Draw("%s>>+histo_unc_down"%args.variable,"%s*%s"%(args.selection,args.weights+"*"+wt_down))


  histo_nominal.SetDirectory(0)
  histo_unc_up.SetDirectory(0)
  histo_unc_down.SetDirectory(0)

nom_yield = histo_nominal.Integral()
histo_nominal.Scale(1./nom_yield)
if doUncerts:
    print histo_unc_up.Integral()
    histo_unc_up.Scale(1./nom_yield) #Scale to nominal to take into account norm effects of the uncerts too
    histo_unc_down.Scale(1./nom_yield) #Scale to nominal to take into account norm effects of the uncerts too
    print histo_unc_up.Integral()


canvas = ROOT.TCanvas("c1","c1")
pads = plot.TwoPadSplit(0.29,0.01,0.01)
axish = createAxisHists(2,histo_nominal,histo_nominal.GetXaxis().GetXmin(),histo_nominal.GetXaxis().GetXmax()-0.01)
axish[0].GetYaxis().SetRangeUser(0,1.4*histo_nominal.GetMaximum())
axish[0].GetYaxis().SetTitle("a.u.")
axish[0].GetXaxis().SetTitleSize(0)
axish[0].GetXaxis().SetLabelSize(0)
axish[1].GetXaxis().SetTitle("%s"%args.xlabel)
axish[1].GetYaxis().SetTitle("ratio")
axish[1].GetYaxis().SetRangeUser(0.93,1.07)


if doUncerts:
    ratio_up = plot.MakeRatioHist(histo_unc_up,histo_nominal,True,False)
    ratio_down = plot.MakeRatioHist(histo_unc_down,histo_nominal,True,False)
    ratio_up.SetLineColor(ROOT.kRed)
    ratio_down.SetLineColor(ROOT.kRed)

pads[0].cd()
axish[0].Draw()
histo_nominal.Draw("SAME")
if doUncerts:
    histo_unc_up.Draw("SAME")
    histo_unc_down.Draw("SAME")
#LHE_ht_ghost.Draw("SAME")
legend = plot.PositionedLegend(0.3, 0.15, 3, 0.015)
legend.AddEntry(histo_nominal, "Nominal")
if args.uncerts is not None:
    if 'nlo' in args.uncerts:
        legend.AddEntry(histo_unc_up,"LO to NLO wt Up/Down")
    elif 'wrew' in args.uncerts:
        legend.AddEntry(histo_unc_up,"W pT reweighting Up/Down")
    elif 'scale' in args.uncerts:
        legend.AddEntry(histo_unc_up,"MuRMuF Up/Down")
legend.Draw("SAME")

pads[1].cd()
axish[1].Draw()
if doUncerts:
    ratio_up.Draw("HISTSAME")
    ratio_down.Draw("HISTSAME")

pads[0].cd()
pads[0].GetFrame().Draw()
pads[0].RedrawAxis()

if args.uncerts is not None:
    if 'nlo' in args.uncerts:
        outf = ROOT.TFile("%s_lotonlo.root"%(args.variable),"RECREATE")
        histo_unc_up.SetNameTitle("%s_lotonlo_up"%(args.variable),"%s_lotonlo_up"%(args.variable))
        histo_unc_down.SetNameTitle("%s_lotonlo_down"%(args.variable),"%s_lotonlo_down"%(args.variable))
        histo_nominal.SetNameTitle("%s"%(args.variable),"%s"%(args.variable))
        histo_unc_up.Write()
        histo_unc_down.Write()
        histo_nominal.Write()
        outf.Close()
    if 'wrew' in args.uncerts:
        outf = ROOT.TFile("%s_wptrew.root"%(args.variable),"RECREATE")
        histo_unc_up.SetNameTitle("%s_wptrew_up"%(args.variable),"%s_wptrew_up"%(args.variable))
        histo_unc_down.SetNameTitle("%s_wptrew_down"%(args.variable),"%s_wptrew_down"%(args.variable))
        histo_unc_up.Write()
        histo_unc_down.Write()
        outf.Close()
    if 'scale' in args.uncerts:
        outf = ROOT.TFile("%s_scale.root"%(args.variable),"RECREATE")
        histo_unc_up.SetNameTitle("%s_scale_up"%(args.variable),"%s_scale_up"%(args.variable))
        histo_unc_down.SetNameTitle("%s_scale_down"%(args.variable),"%s_scale_down"%(args.variable))
        histo_unc_up.Write()
        histo_unc_down.Write()
        outf.Close()
else:
    outf = ROOT.TFile("%s%s.root"%(args.variable,args.outnextra),"RECREATE")
    histo_nominal.SetNameTitle("%s%s"%(args.variable,args.outnextra),"%s%s"%(args.variable,args.outnextra))
    histo_nominal.Write()
    outf.Close()
       

canvas.SaveAs("%s%s.pdf"%(args.variable,args.outnextra))
canvas.SaveAs("%s%s.png"%(args.variable,args.outnextra))
