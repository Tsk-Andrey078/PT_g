import requests
from bs4 import BeautifulSoup

def parse_link(row):
    print(row["top_tag"])
    url = row["RESOURCE_URL"]
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    top_tag = row["top_tag"].split('/')
    i1 = 0
    for path_elem in top_tag:
        array = path_elem.split('::')
        if array[1] == "none" or array[2] == "none":
            
            # If in the path we have more than 1 element, at the next process we search our element in the result of the first iteration
            if i1 == 1:
                res = str(top_tag_parse)
                temp = BeautifulSoup(res, "html.parser")
                top_tag_parse = temp.find_all(array[0])
            # ========================================================

            # If it's the first iteration, we just search our element in a response of request(I mean in all HTML document)
            else:
                top_tag_parse = soup.find_all(array[0])
            #=========================================================

        else:
            if i1 == 1:
                res = str(top_tag_parse)
                temp = BeautifulSoup(res, "html.parser")
                top_tag_parse = temp.find_all(array[0], {array[1]: array[2]})
            else:
                top_tag_parse = soup.find_all(array[0], {array[1]: array[2]})
        i1 = 1
        
    res = str(top_tag_parse)
    temp = BeautifulSoup(res, "html.parser")
    top_tag_parse = temp.find_all("a")
    return top_tag_parse

def parse_title(row):
    print(row["title_cut"])
    url = row["RESOURCE_URL"]
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    title_cut = row["title_cut"].split('/')
    i1 = 0
    for path_elem in title_cut:
        array = path_elem.split('::')
        if array[1] == "none" or array[2] == "none":
            if i1 == 1:
                res = str(title_cut_parse)
                temp = BeautifulSoup(res, "html.parser")
                title_cut_parse = temp.find_all(array[0])
            else:
                title_cut_parse = soup.find_all(array[0])
        else:
            if i1 == 1:
                res = str(title_cut_parse)
                temp = BeautifulSoup(res, "html.parser")
                title_cut_parse = temp.find_all(array[0], {array[1]: array[2]})
            else:
                title_cut_parse = soup.find_all(array[0], {array[1]: array[2]})
        i1 = 1
    return title_cut_parse

def parse_date(row):
    print(row["date_cut"])
    url = row["RESOURCE_URL"]
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    date_cut = row["date_cut"].split('/')
    i1 = 0
    for path_elem in date_cut:
        array = path_elem.split("::")
        if array[1] == "none" or array[2] == "none":
            if i1 == 1:
                res = str(date_cut_parse)
                temp = BeautifulSoup(res, "html.parser")
                date_cut_parse = temp.find_all(array[0])
            else:
                date_cut_parse = soup.find_all(array[0])
        else:
            if i1 == 1:
                res = str(date_cut_parse)
                temp = BeautifulSoup(res, "html.parser")
                date_cut_parse = temp.fina_all(array[0], {array[1]: array[2]})
            else:    
                date_cut_parse = soup.find_all(array[0], {array[1]: array[2]})
        i1 = 1
    return date_cut_parse

def parse_bottom(row):
    print(row["bottom_tag"])
    url = row["RESOURCE_URL"]
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    bottom_tag = row["bottom_tag"].split('/')
    i1 = 0
    for path_elem in bottom_tag:
        array = path_elem.split("::")
        if array[1] == "none" or array[2] == "none":
            if i1 == 1:
                res = str(bottom_tag_parse)
                temp = BeautifulSoup(res, "html.parser")
                bottom_tag_parse = temp.find_all(array[0])
            else:
                bottom_tag_parse = soup.find_all(array[0])
        else:
            if i1 == 1:
                res = str(bottom_tag_parse)
                temp = BeautifulSoup(res, "html.parser")
                bottom_tag_parse = temp.find_all(array[0], {array[1]: array[2]})
            else:    
                bottom_tag_parse = soup.find_all(array[0], {array[1]: array[2]})
        i1 = 1
    return bottom_tag_parse