import os 

#Without weights
os.system('python makeVHFPlotsOpts.py --nbins=10 --xmin=60 --xmax=160 --variable H_mass --weights "intWeight" --outnextra "_noweight" --xlabel "m_{bb} [GeV]"')
os.system('python makeVHFPlotsOpts.py --nbins=15 --xmin=150 --xmax=450 --variable V_pt --weights "intWeight" --outnextra "_noweight" --xlabel "W p_{T} [GeV]"')
os.system('python makeVHFPlotsOpts.py --nbins=15 --xmin=0 --xmax=150 --variable H_pt --weights "intWeight" --outnextra "_noweight" --xlabel "p^{bb}_{T} [GeV]"')
os.system('python makeVHFPlotsOpts.py --nbins=10 --xmin=-0.5 --xmax=9.5 --variable nAddJets --weights "intWeight" --outnextra "_noweight" --xlabel "N_{jets} (additional)" --selection "(V_pt>150)" ')

#With WJetNLOweight
os.system('python makeVHFPlotsOpts.py --nbins=10 --xmin=60 --xmax=160 --variable H_mass --weights "intWeight*WJetNLOWeight" --outnextra "_NLOwt" --xlabel "m_{bb} [GeV]"')
os.system('python makeVHFPlotsOpts.py --nbins=15 --xmin=150 --xmax=450 --variable V_pt --weights "intWeight*WJetNLOWeight" --outnextra "_NLOwt" --xlabel "W p_{T} [GeV]"')
os.system('python makeVHFPlotsOpts.py --nbins=15 --xmin=0 --xmax=150 --variable H_pt --weights "intWeight*WJetNLOWeight" --outnextra "_NLOwt" --xlabel "p^{bb}_{T} [GeV]"')
os.system('python makeVHFPlotsOpts.py --nbins=10 --xmin=-0.5 --xmax=9.5 --variable nAddJets --weights "intWeight*WJetNLOWeight" --outnextra "_NLOwt" --xlabel "N_{jets} (additional)" --selection "(V_pt>150)" ')

#with W reweighting
os.system('python makeVHFPlotsOpts.py --nbins=10 --xmin=60 --xmax=160 --variable H_mass --weights "intWeight*recoWReWeight" --outnextra "_WpTwt" --xlabel "m_{bb} [GeV]"')
os.system('python makeVHFPlotsOpts.py --nbins=15 --xmin=150 --xmax=450 --variable V_pt --weights "intWeight*recoWReWeight" --outnextra "_WpTwt" --xlabel "W p_{T} [GeV]"')
os.system('python makeVHFPlotsOpts.py --nbins=15 --xmin=0 --xmax=150 --variable H_pt --weights "intWeight*recoWReWeight" --outnextra "_WpTwt" --xlabel "p^{bb}_{T} [GeV]"')
os.system('python makeVHFPlotsOpts.py --nbins=10 --xmin=-0.5 --xmax=9.5 --variable nAddJets --weights "intWeight*recoWReWeight" --outnextra "_WpTwt" --xlabel "N_{jets} (additional)" --selection "(V_pt>150)" ')

#with EWK weights
os.system('python makeVHFPlotsOpts.py --nbins=10 --xmin=60 --xmax=160 --variable H_mass --weights "intWeight*weight_ptEWK" --outnextra "_EWKwt"  --xlabel "m_{bb} [GeV]" ')
os.system('python makeVHFPlotsOpts.py --nbins=15 --xmin=150 --xmax=450 --variable V_pt --weights "intWeight*weight_ptEWK" --outnextra "_EWKwt" --xlabel "W p_{T} [GeV]"')
os.system('python makeVHFPlotsOpts.py --nbins=15 --xmin=0 --xmax=150 --variable H_pt --weights "intWeight*weight_ptEWK" --outnextra "_EWKwt" --xlabel "p^{bb}_{T} [GeV]"')
os.system('python makeVHFPlotsOpts.py --nbins=10 --xmin=-0.5 --xmax=9.5 --variable nAddJets --weights "intWeight*weight_ptEWK" --outnextra "_EWKwt" --xlabel "N_{jets} (additional)" --selection "(V_pt>150)" ')

#with all weights - scale uncerts
os.system('python makeVHFPlotsOpts.py --nbins=10 --xmin=60 --xmax=160 --variable H_mass --weights "intWeight*WJetNLOWeight*recoWReWeight*weight_ptEWK" --outnextra "_all_scaleuncert" --uncerts scale --xlabel "m_{bb} [GeV]" ')
os.system('python makeVHFPlotsOpts.py --nbins=15 --xmin=150 --xmax=450 --variable V_pt --weights "intWeight*WJetNLOWeight*recoWReWeight*weight_ptEWK" --outnextra "_all_scaleuncert" --uncerts scale --xlabel "W p_{T} [GeV]"')
os.system('python makeVHFPlotsOpts.py --nbins=15 --xmin=0 --xmax=150 --variable H_pt --weights "intWeight*WJetNLOWeight*recoWReWeight*weight_ptEWK" --outnextra "_all_scaleuncert" --uncerts scale --xlabel "p^{bb}_{T} [GeV]"')
os.system('python makeVHFPlotsOpts.py --nbins=10 --xmin=-0.5 --xmax=9.5 --variable nAddJets --weights "intWeight*WJetNLOWeight*recoWReWeight*weight_ptEWK" --outnextra "_all_scaleuncert" --uncerts scale --xlabel "N_{jets} (additional)" --selection "(V_pt>150)" ')

#with all weights - NLO weight unc
os.system('python makeVHFPlotsOpts.py --nbins=10 --xmin=60 --xmax=160 --variable H_mass --weights "intWeight*WJetNLOWeight*recoWReWeight*weight_ptEWK" --outnextra "_all_NLOuncert" --uncerts nlo --xlabel "m_{bb} [GeV]" ')
os.system('python makeVHFPlotsOpts.py --nbins=15 --xmin=150 --xmax=450 --variable V_pt --weights "intWeight*WJetNLOWeight*recoWReWeight*weight_ptEWK" --outnextra "_all_NLOuncert" --uncerts nlo --xlabel "W p_{T} [GeV]"')
os.system('python makeVHFPlotsOpts.py --nbins=15 --xmin=0 --xmax=150 --variable H_pt --weights "intWeight*WJetNLOWeight*recoWReWeight*weight_ptEWK" --outnextra "_all_NLOuncert" --uncerts nlo --xlabel "p^{bb}_{T} [GeV]"')
os.system('python makeVHFPlotsOpts.py --nbins=10 --xmin=-0.5 --xmax=9.5 --variable nAddJets --weights "intWeight*WJetNLOWeight*recoWReWeight*weight_ptEWK" --outnextra "_all_NLOuncert" --uncerts nlo --xlabel "N_{jets} (additional)" --selection "(V_pt>150)" ')

#with all weights - W reweighting
os.system('python makeVHFPlotsOpts.py --nbins=10 --xmin=60 --xmax=160 --variable H_mass --weights "intWeight*WJetNLOWeight*recoWReWeight*weight_ptEWK" --outnextra "_all_WpTuncert" --uncerts wrew --xlabel "m_{bb} [GeV]" ')
os.system('python makeVHFPlotsOpts.py --nbins=15 --xmin=150 --xmax=450 --variable V_pt --weights "intWeight*WJetNLOWeight*recoWReWeight*weight_ptEWK" --outnextra "_all_WpTuncert" --uncerts wrew --xlabel "W p_{T} [GeV]"')
os.system('python makeVHFPlotsOpts.py --nbins=15 --xmin=0 --xmax=150 --variable H_pt --weights "intWeight*WJetNLOWeight*recoWReWeight*weight_ptEWK" --outnextra "_all_WpTuncert" --uncerts wrew --xlabel "p^{bb}_{T} [GeV]"')
os.system('python makeVHFPlotsOpts.py --nbins=10 --xmin=-0.5 --xmax=9.5 --variable nAddJets --weights "intWeight*WJetNLOWeight*recoWReWeight*weight_ptEWK" --outnextra "_all_WpTuncert" --uncerts wrew --xlabel "N_{jets} (additional)" --selection "(V_pt>150)" ')
