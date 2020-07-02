import requests

def is_valid(handle):
	site_url = 'https://toph.co/u/' # check for toph handle 
	url = site_url + handle  # modify the url for your target site
	res="Invalid";
	request = requests.get(url)
	if request.status_code == 200:
		res = "Valid"
	return res
    
    
if __name__ == "__main__":
    # Open file on read mode            
    input_file = open('data/handle.txt')
    
    #open file in write mode
    out = open('data/checked_handle.txt', 'w') 
    out_valid = open('data/valid_handle.txt', 'w')
    out_invalid = open('data/invalid_handle.txt', 'w')
    
    print("File Processing...")
    lines = input_file.read().split("\n") # Create a list containing all lines
    cnt = -1  # for remove the last newline as handle
    for han in lines:
        #print(han)
        req = is_valid(han)
        res = han + ' : ' + req
        out_line = res+'\n'
        out.write(out_line)
        
        if req == "Valid":
            out_valid.write(out_line)
        else:
            cnt = cnt+1
            out_invalid.write(out_line)
        
    
    
    print("Done!")
    print(cnt, "invalid handle found!")
    
    # Close files
    input_file.close()   
    out.close()
    out_valid.close()
    out_invalid.close()
