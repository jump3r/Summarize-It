

def get_summary(query_text):

	result = query_text.strip().split(".")
	summary = {}
	for i in range(len(result)):
		summary[i] = result[i]
	
	return summary