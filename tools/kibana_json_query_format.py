# NEW TOOL IDEA: create a tool to take in JSON (like a rate error) and then convert it to a valid string you can use to search within in kibana

# for example, a query like this in kibana: 
example = """
msg.user.id:231141 && msg.response.body: "{\"carrier\":\"Sendle\",\"carrier_account_id\":\"ca_69a1aaaa60544866bc7e3eb4bdf5d5c0\",\"type\":\"rate_error\",\"message\":\"Carrier did not respond within 10 seconds.\"}"
"""

data = input("\nEnter the JSON text you want to format for use in a kibana query (without wrapped quotes - quotes will wrap your entered text):\n")

print(data)