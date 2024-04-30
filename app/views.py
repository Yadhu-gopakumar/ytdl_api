
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from pytube import YouTube
import json

@api_view(["POST"])
def api(request):
    try:
        link=request.POST['url']
        try: 
            video = YouTube(link)
            list_opt=[]
            for i in video.streams:

                item=i.__dict__
                selected_item={
                  "url":item["url"],
                   "filesize":item["_filesize_mb"],
                  "resolution":item["resolution"]  ,
                  "mime_type":item["mime_type"]
                }
                list_opt.append(selected_item)

            return Response(list_opt)

        except: 
            print("Some Error!")
            return Response("invalid url")

    except: 
        return Response("Internal request error")


   

    
    
   