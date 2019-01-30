from metrorail import *

# Instantiation of stations
######################################
stations1 = open('stations.dat', 'r')
stations = stations1.readlines()
stations1.close()

final = []
for i in stations:
	x = i.split(",")
	final.append(x)

for i in final:
	i[-1] = i[-1].rstrip("\n")

for i in final:
	exec(('{0} = Station("{1}", "{2}")').format(i[-1].lower(), i[1], i[2]))

########################################

########################################
# Instantiations of Lines
northern_MTV = Line("Bellville via Monte Vista", "green", "28")
northern_MUT = Line("Bellville via Mutual", "green", "23")
central_BLV = Line("Bellville via Lavistown", "blue", "90")
central_KPT = Line("Kapteinsklip via Pinelands", "blue", "95")
central_CHN = Line("Chris Hani via Esplanade", "blue", "99")
southern = Line("Simonstown via Retreat", "red", "1")
cape_flats = Line("Retreat via Pinelands", "brown", "5") 
#########################################

#########################################
# Assigning stations to its respective lines.
# Setting random times between stations.
northern_MUT.set_stations([cpt,wsk,slt,koe,mai,wol,mut,ttn,gdw,vas,els,prw,tyg,blv])
northern_MUT.set_random_travel_times()

northern_MTV.set_stations([cpt,esp,yst,ken,ctc,aka,mtv,dgd,avo,ooz,blv])
northern_MTV.set_random_travel_times()

central_BLV.set_stations([cpt,esp,yst,mut,lng,btw,lvs,blh,uni,pen,srp,blv])
central_BLV.set_random_travel_times()

central_KPT.set_stations([cpt,wsk,slt,koe,mai,ndb,pnl,lng,btw,net,hdv,nya,ppi,ltg,mpl,kpt])
central_KPT.set_random_travel_times()

central_CHN.set_stations([cpt,esp,yst,mut,lng,btw,net,hdv,nya,ppi,sto,man,nol,nkq,khy,kuy,chn])
central_CHN.set_random_travel_times()

southern.set_stations([cpt,wsk,slt,obs,mow,rsb,rdb,new,clr,har,knw,wyn,wit,plm,sth,dpr,htf,ret,stb,lks,fsb,mzb,stj,kkb,fsh,snc,glc,sim])
southern.set_random_travel_times()

cape_flats.set_stations([cpt,wsk,slt,koe,mai,ndb,pnl,haz,ath,crw,lnd,wet,ott,stf,htf,ret])
cape_flats.set_random_travel_times()



all_lines = [northern_MUT, northern_MTV, central_BLV, central_KPT, central_CHN, southern, cape_flats]
###########################################


# Debug Loop to print stations, nb_of stations and end_points.
# Change len to respective check and the print i.respective_check.
'''
for i in network_lines:
	length = len(i.stations)
	print("NEXT*******************")
	print(i.long_name)
	print(length)
	for z in range(length):
		print(i.stations[z].name)
'''
