import boto3
import uuid
import requests
import time

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

    response = transcribe_new.get_transcription_job(TranscriptionJobName=jobName )
    return response

# purpose: get and return the transcript structure given the provided uri
def getTranscript(transcriptURI ):
    # Get the resulting Transcription Job and store the JSON response in transcript
    result = requests.get( transcriptURI )

    return result.text
