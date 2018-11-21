import math

#input all in angular frequency, based on the assumption that they should be in the same case
JJ=6.175*math.pi*2 #MHz
kff=30*math.pi*2 #MHz
Dff=5*math.pi*2 #MHz
offsetz1=300000


freqs1=[6.4463,6.4941,6.5424,6.5915,6.6413,6.6914 ]

cin=[]
cc=[]
for j in range(6):    
       wf=freqs1[j]*2*math.pi #p110 of sank: wf/2pi=6.75GHz
       epsilonr=11.4
       epsiloneff=(1+epsilonr)/2
      # print("pi: %s" %(math.pi))
      # print("sqrt: %s" %(math.sqrt(1.44)))
       cavitylen=math.pi*3e8/(2*wf*math.sqrt(epsiloneff))
       cavitylenflip=math.pi*3e8/(2*(wf-Dff/1000)*math.sqrt(epsiloneff))  #wf*0.995


       qcf=wf*1000/kff #both are in angular frequency
       cinwf=math.sqrt( math.pi/(qcf*2*wf*1e9*wf*1e9*50*50) ) #suppose both are in anglar frequency

       #qcfb=wf/(2*math.pi)*1000/(kff/(2*math.pi) ) #both are in MHz
       cinwfb=math.sqrt( math.pi/(qcf*2*wf/(2*math.pi)*1e9*wf/(2*math.pi)*1e9*50*50) )

       ccwf=2*math.pi*JJ*1e6/(wf*1e9*(wf*1e9-Dff*1e6)*50) #/(2*math.pi) #suppose both are in anglar frequency
       ccwfb=2*math.pi*JJ/(2*math.pi)*1e6/(wf/(2*math.pi)*1e9*(wf/(2*math.pi)*1e9-Dff/(2*math.pi)*1e6)*50)


       cc1=math.pi/(4* wf/(2*math.pi)*1e9  *50)
       cc2=math.pi/(4* (wf/(2*math.pi)*1e9- Dff/(2*math.pi)*1e6 )  *50)
       ccwfc=2*JJ/(2*math.pi)*1e6/0.25/(   math.sqrt( (wf*1e9*(wf*1e9-Dff*1e6) )/(cc1*cc2)  )   )
       print("Cinwf1: %s" %(cinwf) )
       cin.append(cinwf)
       #print("Cinwf1b: %s" %(cinwfb) )
       print("cc1: %s" %(ccwf) )
       #print("cc1b: %s" %(ccwfb) )
       print("cc1c: %s" %(ccwfc) )
       cc.append(ccwfc)


print("\\\\\\")
print(cin)
print("cin mean: %s" %(sum(cin)/6) )
    
print(cc)
print("cc mean: %s" %(sum(cc)/6) )

#for item in cc:
#      print(item)
print("sec2:")


cin=[]
cc=[]

freqs2=[6.7429,6.795,6.848,6.9019,6.9565,7.0119]
for j in range(6):    
       wf=freqs2[j]*2*math.pi #p110 of sank: wf/2pi=6.75GHz
       epsilonr=11.4
       epsiloneff=(1+epsilonr)/2
      # print("pi: %s" %(math.pi))
      # print("sqrt: %s" %(math.sqrt(1.44)))
       cavitylen=math.pi*3e8/(2*wf*math.sqrt(epsiloneff))
       cavitylenflip=math.pi*3e8/(2*(wf-Dff/1000)*math.sqrt(epsiloneff))  #wf*0.995


       qcf=wf*1000/kff #both are in MHz
       cinwf=math.sqrt( math.pi/(qcf*2*wf*1e9*wf*1e9*50*50) ) #suppose both are in anglar frequency

       #qcfb=wf/(2*math.pi)*1000/(kff/(2*math.pi) ) #both are in MHz
       cinwfb=math.sqrt( math.pi/(qcf*2*wf/(2*math.pi)*1e9*wf/(2*math.pi)*1e9*50*50) )

       ccwf=2*math.pi*JJ*1e6/(wf*1e9*(wf*1e9-Dff*1e6)*50) #/(2*math.pi) #suppose both are in anglar frequency
       ccwfb=2*math.pi*JJ/(2*math.pi)*1e6/(wf/(2*math.pi)*1e9*(wf/(2*math.pi)*1e9-Dff/(2*math.pi)*1e6)*50)

       cc1=math.pi/(4* wf/(2*math.pi)*1e9  *50)
       cc2=math.pi/(4* (wf/(2*math.pi)*1e9- Dff/(2*math.pi)*1e6 )  *50)
       ccwfc=2*JJ/(2*math.pi)*1e6/0.25/(   math.sqrt( (wf*1e9*(wf*1e9-Dff*1e6) )/(cc1*cc2)  )   )
       print("Cinwf2: %s" %(cinwf) )
       cin.append(cinwf)
       #print("Cinwf1b: %s" %(cinwfb) )
       print("cc2: %s" %(ccwf) )
       #print("cc1b: %s" %(ccwfb) )
       print("cc2c: %s" %(ccwfc) )
       cc.append(ccwfc)



print("\\\\\\")
print(cin)
print("cin mean: %s" %(sum(cin)/6) )
    
print(cc)
print("cc mean: %s" %(sum(cc)/6) )




print("sec3:")


cin=[]
cc=[]

freqs3=[6.4249,6.4723,6.5205,6.5693,6.6234,6.6738]
for j in range(6):    
       wf=freqs3[j]*2*math.pi #p110 of sank: wf/2pi=6.75GHz
       epsilonr=11.4
       epsiloneff=(1+epsilonr)/2
      # print("pi: %s" %(math.pi))
      # print("sqrt: %s" %(math.sqrt(1.44)))
       cavitylen=math.pi*3e8/(2*wf*math.sqrt(epsiloneff))
       cavitylenflip=math.pi*3e8/(2*(wf-Dff/1000)*math.sqrt(epsiloneff))  #wf*0.995


       qcf=wf*1000/kff #both are in MHz
       cinwf=math.sqrt( math.pi/(qcf*2*wf*1e9*wf*1e9*50*50) ) #suppose both are in anglar frequency

       #qcfb=wf/(2*math.pi)*1000/(kff/(2*math.pi) ) #both are in MHz
       cinwfb=math.sqrt( math.pi/(qcf*2*wf/(2*math.pi)*1e9*wf/(2*math.pi)*1e9*50*50) )

       ccwf=2*math.pi*JJ*1e6/(wf*1e9*(wf*1e9-Dff*1e6)*50) #/(2*math.pi) #suppose both are in anglar frequency
       ccwfb=2*math.pi*JJ/(2*math.pi)*1e6/(wf/(2*math.pi)*1e9*(wf/(2*math.pi)*1e9-Dff/(2*math.pi)*1e6)*50)

       cc1=math.pi/(4* wf/(2*math.pi)*1e9  *50)
       cc2=math.pi/(4* (wf/(2*math.pi)*1e9- Dff/(2*math.pi)*1e6 )  *50)
       ccwfc=2*JJ/(2*math.pi)*1e6/0.25/(   math.sqrt( (wf*1e9*(wf*1e9-Dff*1e6) )/(cc1*cc2)  )   )
       print("Cinwf3: %s" %(cinwf) )
       cin.append(cinwf)
       #print("Cinwf1b: %s" %(cinwfb) )
       print("cc3: %s" %(ccwf) )
       #print("cc1b: %s" %(ccwfb) )
       print("cc3c: %s" %(ccwfc) )
       cc.append(ccwfc)

print("\\\\\\")
print(cin)
print("cin mean: %s" %(sum(cin)/6) )
    
print(cc)
print("cc mean: %s" %(sum(cc)/6) )


print("sec4:")

cin=[]
cc=[]

freqs4=[6.7249,6.7769,6.825,6.8786,6.933,6.9886]
for j in range(6):    
       wf=freqs4[j]*2*math.pi #p110 of sank: wf/2pi=6.75GHz
       epsilonr=11.4
       epsiloneff=(1+epsilonr)/2
      # print("pi: %s" %(math.pi))
      # print("sqrt: %s" %(math.sqrt(1.44)))
       cavitylen=math.pi*3e8/(2*wf*math.sqrt(epsiloneff))
       cavitylenflip=math.pi*3e8/(2*(wf-Dff/1000)*math.sqrt(epsiloneff))  #wf*0.995


       qcf=wf*1000/kff #both are in MHz
       cinwf=math.sqrt( math.pi/(qcf*2*wf*1e9*wf*1e9*50*50) ) #suppose both are in anglar frequency

       #qcfb=wf/(2*math.pi)*1000/(kff/(2*math.pi) ) #both are in MHz
       cinwfb=math.sqrt( math.pi/(qcf*2*wf/(2*math.pi)*1e9*wf/(2*math.pi)*1e9*50*50) )

       ccwf=2*math.pi*JJ*1e6/(wf*1e9*(wf*1e9-Dff*1e6)*50) #/(2*math.pi) #suppose both are in anglar frequency
       ccwfb=2*math.pi*JJ/(2*math.pi)*1e6/(wf/(2*math.pi)*1e9*(wf/(2*math.pi)*1e9-Dff/(2*math.pi)*1e6)*50)

       cc1=math.pi/(4* wf/(2*math.pi)*1e9  *50)
       cc2=math.pi/(4* (wf/(2*math.pi)*1e9- Dff/(2*math.pi)*1e6 )  *50)
       ccwfc=2*JJ/(2*math.pi)*1e6/0.25/(   math.sqrt( (wf*1e9*(wf*1e9-Dff*1e6) )/(cc1*cc2)  )   )
       print("Cinwf4: %s" %(cinwf) )
       cin.append(cinwf)
       #print("Cinwf1b: %s" %(cinwfb) )
       print("cc4: %s" %(ccwf) )
       #print("cc1b: %s" %(ccwfb) )
       print("cc4c: %s" %(ccwfc) )
       cc.append(ccwfc)


print("\\\\\\")
print(cin)
print("cin mean: %s" %(sum(cin)/6) )
    
print(cc)
print("cc mean: %s" %(sum(cc)/6) )
