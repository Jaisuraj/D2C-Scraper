import pandas as pd
import requests

class D2C:

    def __init__(self):
        self.page = 1

    def set_url(self):
        return f"https://dare2compete.com/api/public/opportunity/search-new?opportunity=hackathons&sort=&dir=&filters=Open&types=oppstatus&atype=explore&page={self.page}&showOlderResultForSearch=false"
    def make_request(self):
        url= self.set_url()
        return requests.request("GET",url)
    def get_data(self):
        self.data= self.make_request().json()

    def Scrapper(self,pages):
        name = []
        start_date = []
        end_date = []
        reg_status = []
        rem = []
        seo_url = []
        for page in range(1,pages+1):
            self.make_request()
            self.get_data()
            for item in self.data['data']['data']:
                name.append(item['title'])
                start_date.append(item['start_date'][0:10])
                end_date.append(item['end_date'][0:10])
                reg_status.append(item['regnRequirements']['reg_status'])
                rem.append(item['regnRequirements']['remain_days'])
                seo_url.append(item['seo_url'])
                print("Name:",name,"Start date:",start_date[0:10], "End Date:", end_date[0:10],"Registration Status:", reg_status,"Remaining Days: ",rem,"URL:", seo_url)

            self.page += 1
        df = pd.DataFrame(name, columns=['Name'])
        df['Start-date(yyyy/mm/dd)'] = start_date
        df['End-date(yyyy/mm/dd)'] = end_date
        df['Registration status'] = reg_status
        df['Remaining Days'] = rem
        df['Event Url'] = seo_url


        df.to_csv('data.csv', index=False)

scrapper= D2C()
scrapper.Scrapper(10)
