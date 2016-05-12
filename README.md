# simulated-annealing
<!DOCTYPE html>
<html>
  <head>
    <title>TSP SA</title>
    <meta name="viewport" content="initial-scale=1.0">
    <meta charset="utf-8">

  </head>
  <body>
    <div id="map">
	<textarea id="path" rows="38" ></textarea>
	<img id="mapimg" src="https://maps.googleapis.com/maps/api/staticmap?center=India&size=800x800"/>
	</div>
    <script>
	
	var city_string = "Agartala|Amravathi|Aizawl|Bengaluru|Bhopal|Bhubaneswar|Chandigarh|Chennai|Daman|Dehradun|Dispur|Gandhinagar|Gangtok|Hyderabad|Imphal|Itanagar|Jaipur|Kohima|Kolkata|Lucknow|Mumbai|Nagpur|New+Delhi|Panaji|Patna|Puducherry|Raipur|Ranchi|Shillong|Shimla|Silvassa|Srinagar|Jammu|Thiruvananthapuram";
	var cities = city_string.split("|");
	var distances = [[0, 2765367, 347486, 3385655, 2559659, 1957959, 2697645, 3177694, 3260087, 2443828, 551176, 3052992, 1094985, 2907725, 538779, 837914, 2498530, 645162, 1542363, 1889879, 3330979, 2405333, 2448525, 3751716, 1444512, 3334283, 2152744, 1613119, 464727, 2796883, 3256332, 3291371, 3041096, 3938124], [2773600, 0, 2702862, 664140, 1122510, 816372, 2074259, 458728, 1153870, 2042803, 2227836, 1529200, 1902681, 273177, 2704382, 2522653, 1806282, 2569436, 1257642, 1603296, 994447, 773112, 1825140, 927621, 1619579, 615317, 1053856, 1269185, 2313045, 2173498, 1149934, 2667986, 2417711, 1219159], [347808, 2695189, 0, 3315477, 2489481, 1887780, 2627466, 3107516, 3189908, 2373649, 480997, 2982813, 1024807, 2837547, 408296, 742357, 2428351, 549606, 1472184, 1819700, 3260800, 2335154, 2378347, 3681538, 1374333, 3264104, 2082566, 1542940, 394548, 2726705, 3186154, 3221193, 2970918, 3867946], [3488581, 664689, 3417843, 0, 1439212, 1438630, 2390962, 345718, 1139622, 2359506, 2942817, 1514951, 2617662, 569218, 3419363, 3237634, 2122984, 3284417, 1879900, 1919999, 980199, 1089815, 2141842, 589166, 2084239, 377479, 1370559, 1906953, 3028027, 2490200, 1135686, 2984688, 2734414, 730494], [2559192, 1124696, 2488454, 1439553, 0, 1186561, 1037405, 1479983, 704371, 1005949, 2013427, 602772, 1688273, 850275, 2489974, 2308244, 568029, 2355028, 1377286, 667879, 775262, 350939, 788286, 1196000, 978406, 1636572, 631640, 1059802, 2098637, 1136644, 700616, 1631132, 1380857, 2169662], [1958101, 808423, 1887362, 1428711, 1180863, 0, 1937852, 1220749, 1646145, 1906396, 1412336, 1719932, 1087181, 1042099, 1888882, 1707153, 1738736, 1753936, 442142, 1212869, 1763370, 832953, 1688732, 1696544, 804079, 1377338, 548960, 453685, 1497546, 2037090, 1629949, 2531578, 2281303, 1981180], [2695500, 2074203, 2624761, 2389061, 1036513, 1934651, 0, 2429491, 1505862, 166986, 2149735, 1181469, 1824580, 1799783, 2626281, 2444552, 531460, 2491335, 1712288, 804186, 1664962, 1292006, 260150, 2113697, 1313408, 2586080, 1433402, 1461901, 2234945, 112976, 1514101, 593589, 343314, 3119170], [3185391, 457378, 3114652, 348739, 1477338, 1228163, 2429088, 0, 1494805, 2397632, 2639626, 1870134, 2314471, 628005, 3116172, 2934443, 2161110, 2981227, 1669433, 1958124, 1335382, 1127941, 2179968, 944349, 2031370, 170819, 1408684, 1680975, 2724836, 2528326, 1490869, 3022814, 2772539, 774661], [3275273, 1148300, 3204534, 1138227, 718582, 1667361, 1505904, 1491218, 0, 1528468, 2729508, 385776, 2404353, 861365, 3206054, 3024325, 987026, 3071109, 1950694, 1383959, 170457, 814185, 1243479, 725362, 1694487, 1522979, 1112440, 1648834, 2814718, 1605142, 30370, 2099630, 1849356, 1875994], [2442765, 2042365, 2372026, 2357222, 1004675, 1902812, 163125, 2397652, 1509050, 0, 1897000, 1184657, 1571845, 1767944, 2373546, 2191817, 534648, 2238601, 1680450, 561044, 1668149, 1260168, 248344, 2116884, 1109375, 2554241, 1401563, 1430062, 1982210, 224109, 1517289, 786816, 536541, 3087331], [551005, 2222144, 480266, 2842432, 2016436, 1414736, 2154422, 2634471, 2716863, 1900604, 0, 2509769, 551762, 2364502, 481787, 380708, 1955306, 346841, 999140, 1346655, 2787755, 1862110, 1905302, 3208493, 901289, 2791060, 1609521, 1069895, 90450, 2253660, 2713109, 2748148, 2497873, 3394901], [3041879, 1522631, 2971140, 1512557, 596923, 1721595, 1151115, 1865549, 385688, 1173679, 2496114, 0, 2170959, 1210173, 2972660, 2790931, 632236, 2837715, 2032057, 1150565, 544787, 885972, 888689, 1099693, 1633177, 1897310, 1166674, 1781670, 2581324, 1250353, 393927, 1642653, 1392378, 2250325], [1094577, 1893970, 1023838, 2514257, 1688261, 1086561, 1826247, 2306296, 2388689, 1572430, 548812, 2181594, 0, 2036327, 1025358, 843629, 1627132, 890413, 670965, 1018481, 2459581, 1533935, 1577127, 2880319, 573114, 2462885, 1281346, 741721, 634022, 1925485, 2384934, 2419973, 2169698, 3066726], [2899567, 271263, 2828829, 569140, 850198, 1046983, 1801948, 626551, 866658, 1770492, 2353803, 1209972, 2028648, 0, 2830349, 2648620, 1533970, 2695403, 1488253, 1330985, 707235, 500801, 1552828, 664219, 1495225, 783140, 781545, 1317939, 2439013, 1901186, 862722, 2395674, 2145399, 1299249], [540778, 2695294, 409014, 3315582, 2489586, 1887885, 2627571, 3107621, 3190013, 2373754, 481102, 2982918, 1024912, 2837652, 0, 627562, 2428456, 136760, 1472289, 1819805, 3260905, 2335259, 2378452, 3681643, 1374438, 3264209, 2082670, 1543045, 549113, 2726810, 3186259, 3221298, 2971023, 3868051], [837715, 2514601, 741595, 3134888, 2308893, 1707192, 2446878, 2926927, 3009320, 2193061, 380865, 2802225, 844218, 2656958, 627559, 0, 2247763, 492613, 1291596, 1639112, 3080212, 2154566, 2197758, 3500950, 1193745, 3083516, 1901977, 1362352, 448875, 2546116, 3005565, 3040604, 2790329, 3687357], [2498192, 1808603, 2427453, 2123461, 570532, 1737343, 523056, 2163891, 986067, 545621, 1952427, 661674, 1627272, 1534183, 2428974, 2247244, 0, 2294028, 1514981, 606879, 1145167, 1026406, 260631, 1593902, 1116101, 2320480, 1167802, 1264593, 2037637, 622295, 994306, 1116783, 866508, 2853570], [627641, 2560383, 531521, 3180671, 2354675, 1752975, 2492661, 2972710, 3055102, 2238843, 346192, 2848008, 890001, 2702741, 136795, 492651, 2293545, 0, 1337378, 1684894, 3125994, 2200349, 2243541, 3546732, 1239528, 3129299, 1947760, 1408134, 414203, 2591899, 3051348, 3086387, 2836112, 3733140], [1542490, 1248941, 1471752, 1869228, 1376683, 441532, 1714734, 1661267, 1935470, 1683278, 996726, 2043461, 671571, 1482617, 1473272, 1291543, 1515619, 1338326, 0, 989751, 1945684, 1122277, 1465614, 2137061, 580961, 1817856, 838285, 402809, 1081935, 1813972, 1919273, 2308460, 2058185, 2421697], [1889295, 1705516, 1818556, 2020373, 667826, 1211333, 805812, 2060803, 1368253, 561550, 1343530, 1161159, 1018375, 1431096, 1820076, 1638347, 606696, 1685130, 988971, 0, 1439145, 923319, 556692, 1859883, 555905, 2217392, 783294, 738583, 1428740, 905050, 1364499, 1399538, 1149263, 2750482], [3331236, 993990, 3260497, 983916, 774545, 1769710, 1672357, 1336908, 176900, 1694922, 2785471, 552229, 2460316, 707055, 3262017, 3080288, 1153479, 3127072, 1950927, 1439922, 0, 814418, 1409932, 571051, 1750450, 1368668, 1112673, 1649068, 2870681, 1771596, 172964, 2266084, 2015809, 1721684], [2402716, 775267, 2331977, 1090124, 350782, 839607, 1292788, 1130554, 798872, 1261332, 1856951, 889851, 1531796, 500846, 2333497, 2151768, 1024810, 2198552, 1122940, 821825, 809087, 0, 1043669, 1118583, 998374, 1287143, 284686, 821081, 1942161, 1392027, 782675, 1886515, 1636240, 1820233], [2447206, 1825910, 2376468, 2140768, 788220, 1686358, 260207, 2181198, 1242560, 248224, 1901442, 918167, 1576287, 1551490, 2377988, 2196259, 268158, 2243042, 1463995, 555893, 1401659, 1043713, 0, 1850394, 1065115, 2337786, 1185109, 1213608, 1986651, 359446, 1250799, 853934, 603659, 2870877], [3757612, 929813, 3686873, 591147, 1200921, 1705533, 2113880, 944139, 733268, 2136445, 3211847, 1108597, 2886692, 665637, 3688393, 3506664, 1595002, 3553448, 2146803, 1866298, 573844, 1112107, 1851455, 0, 2180658, 975900, 1466977, 2003372, 3297057, 2213119, 729332, 2707607, 2457332, 1328915], [1441618, 1609810, 1370879, 2077920, 972206, 802401, 1310257, 2022136, 1672634, 1110136, 895853, 1638984, 570698, 1488642, 1372399, 1190670, 1111142, 1237454, 580039, 556187, 1743526, 986250, 1061137, 2106379, 0, 2178725, 734758, 335808, 981063, 1409495, 1668879, 1903983, 1653708, 2808029], [3343206, 615193, 3272467, 378120, 1635153, 1385977, 2586902, 169577, 1524186, 2555446, 2797441, 1899515, 2472286, 785820, 3273987, 3092258, 2318925, 3139042, 1827247, 2115939, 1364763, 1285755, 2337783, 973730, 2189184, 0, 1566499, 1838790, 2882651, 2686141, 1520250, 3180629, 2930354, 644193], [2161890, 1054169, 2091152, 1369026, 631587, 555410, 1434248, 1409456, 1096869, 1402792, 1616125, 1170656, 1290971, 779749, 2092672, 1910942, 1166271, 1957726, 838743, 770446, 1107084, 283677, 1185129, 1397485, 734900, 1566045, 0, 541851, 1701335, 1533487, 1080673, 2027975, 1777700, 2099135], [1611989, 1259615, 1541250, 1906005, 1023911, 452206, 1458097, 1671941, 1633847, 1426641, 1066224, 1786824, 741069, 1316727, 1542770, 1361041, 1258982, 1407825, 402459, 733114, 1644062, 820655, 1208977, 1934464, 324325, 1828530, 541926, 0, 1151434, 1557335, 1617651, 2051823, 1801548, 2432372], [466547, 2304678, 395808, 2924966, 2098970, 1497270, 2236956, 2717005, 2799398, 1983139, 90487, 2592303, 634296, 2447036, 550622, 449543, 2037840, 415676, 1081674, 1429189, 2870289, 1944644, 1987836, 3291027, 983823, 2873594, 1692055, 1152429, 0, 2336194, 2795643, 2830682, 2580407, 3477435], [2794772, 2173476, 2724034, 2488333, 1135786, 2033923, 112909, 2528763, 1605135, 224138, 2249007, 1280742, 1923853, 1899056, 2725554, 2543824, 630733, 2590608, 1811561, 903459, 1764234, 1391279, 359422, 2212969, 1412681, 2685352, 1532674, 1561173, 2334217, 0, 1613374, 700105, 449830, 3218442], [3256164, 1144173, 3185425, 1134099, 699473, 1638762, 1516728, 1487091, 30332, 1539293, 2710399, 396600, 2385244, 857238, 3186945, 3005216, 997850, 3052000, 1922095, 1364850, 166329, 785586, 1254303, 721234, 1675377, 1518852, 1083841, 1620235, 2795609, 1615967, 0, 2110455, 1860180, 1871867], [3289241, 2667945, 3218502, 2982802, 1630255, 2528392, 593621, 3023232, 2027875, 783494, 2743476, 1631843, 2418321, 2393524, 3220022, 3038293, 1125201, 3085077, 2306030, 1397927, 2186975, 1885748, 853891, 2707438, 1907150, 3179821, 2027143, 2055642, 2828686, 700005, 2036115, 0, 288821, 3712911], [3037337, 2416041, 2966599, 2730898, 1378351, 2276489, 341717, 2771328, 1775972, 531590, 2491573, 1379939, 2166418, 2141621, 2968119, 2786389, 873298, 2833173, 2054126, 1146024, 1935071, 1633844, 601987, 2455534, 1655246, 2927917, 1775239, 1803738, 2576782, 448102, 1784211, 291803, 0, 3461007], [3946915, 1218901, 3876176, 731186, 2169104, 1989686, 3120854, 773286, 1877252, 3089398, 3401150, 2252582, 3075995, 1299110, 3877696, 3695967, 2738986, 3742750, 2430956, 2649891, 1717829, 1819707, 2871734, 1326796, 2814131, 644732, 2100451, 2442499, 3486360, 3220092, 1873316, 3714580, 3464305, 0]];
	var temp = 1000000;
	var S = new Array(cities.length);
	var Best = S;
	for (var i=0; i<cities.length; i++) {
		S[i] = i;
	}
	var cost_best = cost(Best);
	
	window.setInterval(function(){
		if(temp>0) {
			run_algo();
		}
	}, 1500);


	function range(start, end) {
		var foo = [];
		for (var i = start; i <= end; i++) {
			foo.push(i);
		}
		return foo;
	}
	function gaussian(mu, sigma) {
		var w = 0;
		do {
			var x = Math.random()*2 -1;
			var y = Math.random()*2 -1;
			w = x*x + y*y;
		} while (w<=0 || w>=1);
		return mu + (x*sigma)*Math.sqrt(-2*Math.log(w)/w);
	}
	
	function swap(seq) {
		seq2 = seq.slice();
        a = Math.floor((Math.random()*seq.length));
        b = Math.floor((Math.random()*seq.length));
        t = seq2[a];
        seq2[a] = seq2[b];
        seq2[b] = t;
        return seq2;
	}
	
	function tweak(seq) {
		num_swaps = Math.ceil(Math.abs(gaussian(0,1)));
		for (var i = 0; i < num_swaps; i++) {
			seq = swap(seq);
		}
		return seq;
	}
	
	function cost(seq) {
		dist = 0;
		for (var i=0; i<seq.length; i++) {
			dist = dist + distances[seq[i]][seq[(i+1)%(seq.length)]];
		}
		return dist;
	}
	
	function update_map(seq) {
		var uri = "https://maps.googleapis.com/maps/api/staticmap?center=India&size=800x800&path=color:0xff0000ff|weight:2|";
		var path = "";
        for (var i=0; i<seq.length; i++) {
			uri = uri + cities[seq[i]] + "|";
			path = path + cities[seq[i]] + "\n";
		}
		uri = uri + cities[seq[0]];
		path = path + cities[seq[0]] + "\nTemperature = " +temp + "\nMin. distance=" +cost_best;
		document.getElementById("mapimg").src=uri+"&KEY=AIzaSyBs68-2LsV9f_WmqmJ3PHaPx4bTMNMOuDE ";
		document.getElementById("path").value = path;
	}
	
	function run_algo() {
		while (temp>0 && temp%50000 != 0) {
			R = tweak(S);
			cost_s = cost(S);
			cost_r = cost(R);
			prob = Math.exp((cost_s-cost_r)*1.0/temp);
			if (cost_r < cost_s || Math.random() < prob) {
				S = R;
			}
			temp = temp-25;
			if (cost_r < cost_best) {
				Best = R;
				cost_best = cost_r;
			}
		}
		update_map(S);
		temp = temp-25;
		if (temp<=0) {
			update_map(Best);
		}
	}
    </script>
  </body>
</html>