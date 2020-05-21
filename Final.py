from moviepy.editor import *
import boto3
import uuid
import requests
import time

from transcribeUtils import *
from srtUtils import *

# purpose: Function to format the input parameters and invoke the Transcribe service
def createTranscribeJob():

    # Set up the Transcribe client 
    transcribe_new = boto3.client("transcribe", aws_access_key_id="AKIATF34XXBC4MDLQKET",
                                aws_secret_access_key="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",
                                region_name='ap-south-1')
    
    # Set up the full uri for the bucket and media file
    mediaUri = "https://video-subtitles1.s3.ap-south-1.amazonaws.com/01.+Welcome+DEND-R5o2UFujjq0.mp4" 
    
    print( "Creating Job: " + "transcribe" + mediaUri )
    
    # Use the uuid functionality to generate a unique job name.  Otherwise, the Transcribe service will return an error
    response = transcribe_new.start_transcription_job(TranscriptionJobName="transcribeJob1", \
        LanguageCode = "en-US", \
        MediaFormat = "mp4", \
        Media = { "MediaFileUri" : mediaUri }) 
        #Settings = { "VocabularyName" : "MyVocabulary" } \
        
    
    # return the response structure found in the Transcribe Documentation
    return response
    
    
# purpose: simply return the job status    
def getTranscriptionJobStatus(jobName ):
    transcribe_new = boto3.client("transcribe", aws_access_key_id="AKIATF34XXBC4MDLQKET",
                                aws_secret_access_key="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",
                                region_name="ap-south-1")
    
    response = transcribe_new.response = createTranscribeJob()
    return response

    
    
# purpose: get and return the transcript structure given the provided uri
def getTranscript(transcriptURI ):
    # Get the resulting Transcription Job and store the JSON response in transcript
    result = requests.get(transcriptURI)

    return result.text

# loop until the job successfully completes
print( "\n==> Transcription Job: " + response["TranscriptionJob"]["TranscriptionJobName"] + "\n\tIn Progress"),

while( response["TranscriptionJob"]["TranscriptionJobStatus"] == "IN_PROGRESS"):
    print( "."),
    time.sleep( 30 )
    response = getTranscriptionJobStatus( response["TranscriptionJob"]["TranscriptionJobName"] )

print( "\nJob Complete")
print( "\tStart Time: " + str(response["TranscriptionJob"]["CreationTime"]) )
print( "\tEnd Time: "  + str(response["TranscriptionJob"]["CompletionTime"]) )
print( "\tTranscript URI: " + str(response["TranscriptionJob"]["Transcript"]["TranscriptFileUri"]) )

# Now get the transcript JSON from AWS Transcribe
transcript = getTranscript( str(response["TranscriptionJob"]["Transcript"]["TranscriptFileUri"]) ) 


writeTranscriptToSRT(transcript, 'en', "subtitles-en.srt" )  

#writeTranslationToSRT(transcript,"en","ja","subtitles-jp.srt","ap-south-1") 
    
    
    


