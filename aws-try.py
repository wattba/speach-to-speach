import boto3

translate = boto3.client(service_name='translate', region_name='us-west-2', use_ssl=True)

result = translate.translate_text(Text="Hello, World", 
            SourceLanguageCode="en", TargetLanguageCode="de")
print('TranslatedText: ' + result.get('TranslatedText'))
