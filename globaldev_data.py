import global_development

#question: What was the development rate in Canada in 1980?
#What was the population in Canada in 1980?
#how much is the rural areas of canada growing in 1980?import 

report_list = global_development.get_reports(test=True)

print("Did you know the fertility rate of Canada in 1980?")
print("The fertility rate in Canada in 1980 was", report_list[0]['Data']['Health']['Fertility Rate'])
print("Canada's urban areas where growing more than their rural areas.")
print("Urban percent growth:    ", report_list[0]['Data']['Urban Development']['Urban Population Percent Growth'])
print("Rural percent growth:    ",report_list[0]['Data']['Rural Development']['Rural Population Growth'])
print("This data is unlikely to be biased because it doesn't have any elements that could become biased.")

