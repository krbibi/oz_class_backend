
class PageReplacementFIFO :
    def __init__(self,capacity) :
        self.capacity = capacity
        self.pages = []

    def access_page(self,page) :
        if page not in self.pages:
            if len(self.pages) >= self.capacity :
                self.pages.pop(0) # 제일 앞에 있는 친구를 뺀다
            self.pages.append(page)
    
    def status(self) :
        print('현재 페이지 상태 :',self.pages)

page_replacement = PageReplacementFIFO(capacity=3)

page_replacement.status()

page_replacement.access_page(3)
page_replacement.status()
page_replacement.access_page(2)
page_replacement.status()
page_replacement.access_page(1)
page_replacement.status()
page_replacement.access_page(4)
page_replacement.status()