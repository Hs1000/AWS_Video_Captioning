# AWS_Video_Captioning
Automatically generating captions for videos using the Amazon Transcribe and Amazon Transcribe services using the boto3 client.

# Creating account on amazon web services
First step: We need to have the access_key_id and secret_key_id using account credentials and for all that we have to create account on Amazon web services

# Boto Client
Second Step: Using Boto3 client we will use transcribe service of amazon to generate text from an input video and remember not to forget to mention the region name in the boto3 client from the region you are operating the services.

# JSON File Creation
Third Step: We are left with a json response after downloading the transcript URI that we have to further convert into the SRT Format.
