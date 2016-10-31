#input: seed url
#output: index
def crawl_web(seed): #know what seed is? a start url
	to_crawl=[seed]
	crawled=[]
	index=[]
	while to_crawl:
		page=to_crawl.pop()
		if url not in crawled:
			content=get_page(page)
			add_page_to_index(index, page, content)
			union(to_crawl,get_all_links(get_page(page))) #know what get_page() is? a long code of a html?
			crawled.append(page)
	return	crawled