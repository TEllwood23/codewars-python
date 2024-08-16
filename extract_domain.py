def domain_name(url):
    start_address = ["http://", "https://", "www."]
    end_address = [".com", ".co.uk", ".org", ".co", ".biz", ".info", ".us", ".jp", ".php", ".edu", ".net", ".ru", ".de", ".fr", ".it", ".es"]

    url_new = url


    for item in start_address:
        if item in url:
            url_new = url.split(item)[1]
            break


    for item in end_address:
        if item in url_new:
            url_final = url_new.split(item)[0]
            return url_final
        else:
            url_final = url_new

    return url_new.split('.')[0]

print(f"Test 1 = {domain_name('www.codewars')}")
print(f"Test 2 = {domain_name('http://google.com')}")
