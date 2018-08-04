import copy

d1 = {
	"Mehmood":"halcyoona",
	"Ahmed":"mrcreamio",
	"Ali":"dexturus",
	"Ahsan":"cool",
	"Hamza":"sothsier",
	"Nouman":"Robot"
}


d2 = {
	"Mehmood":"1",
	"Ahmed":"2",
	"Ali":"3",
	"Ahsan":"4",
	"Hamza":"5",
	"Nouman":"6"
}


d3 = {
	"Mehmood":"Munir",
	"Ahmed":"Waheed",
	"Ali":"Husnain",
	"Ahsan":"hot",
	"Hamza":"Qureshi",
	"Nouman":"Afsar"
}



l1 = [d1,d2,d3]

l2 = l1[:]

l3 = copy.deepcopy(l2)

print(l3[0])
print(l1[0])

l2[0]['Mehmood'] = 'good'

print(l1[0])
print(l3[0])