import ast
import requests
from collections import defaultdict

import RSS_praser
import status_logger



def get_NEWS(file_path):
    try:
        with open(file_path) as f:
            RSS_data = f.read()
        RSS_data = ast.literal_eval(RSS_data)
        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
            }

        news = defaultdict(lambda: {
                "Title": "",
                "Description": "",
                "Published_date": "",
                "Link": "",
            })
        
        error_stack=[]
        
        count=0
        for i in RSS_data:
            response = requests.get(RSS_data[i],headers=headers)
            url_data = response.text

            if response.status_code==200:
                result=RSS_praser.check_parse(url_data,news,count)
                if result[0] is None:
                    error_stack.append(result[1])
                else:
                    news, count = result 
            else:
                status_logger.debug_logger('error',f"Error in accessing website {i}: {response.status_code}: LINK = {RSS_data[i]}")
                error_stack.append([response.status_code, i, RSS_data[i]])
                
        status_logger.debug_logger('info', f'Errors encounted {len(error_stack)}')
        if news is None:
            status_logger.debug_logger('info',f"No news to send")
        return news,error_stack
    except Exception as e:
        status_logger.debug_logger('error',f"Unable to open file: {e}")
        return None,None