import json
import perform_action as pa

def parse_request(request):
	if(request["action"] == "send"):
		pa.send_msg(request)
	if(request["action"] == "retrieve"):
		pa.retrieve_msg(request)