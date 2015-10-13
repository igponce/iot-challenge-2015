"""
pushtoazurecdn.py

Push the data to a blob in the Azure CDN (pickled)
Requires the Azure SDK for Python (of course - no black magic here!)

Copyright (C) 2015 Iñigo Gonzalez Ponce <igponce (at) gmail (dot) youknowwhat>

Permission is hereby granted, free of charge, to any person obtaining 
a copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation 
the rights to use, copy, modify, merge, publish, distribute, sublicense,
 and/or sell copies of the Software, and to permit persons to whom the Software
 is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included 
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
DEALINGS IN THE SOFTWARE
"""	

# Configration 
azureAccountKey = '33QfPAWY453Tp3g9VakhwG7Sl6C9fXmndQnBMTSa3N1ezeDG4h7ffb4AxXQbgV4Az4cX850F/dLviLSIa2FxgA=='
azureAccount    = 'iotenergydemo'
azureContainer  = 'energyprice' # URL: https://iotenergydemo.blob.core.windows.net/energyprice
azureFile       = 'precios.pickle'

import pickle
from azure.storage.blob import BlobService

def pushToAzureCDN (data):

	blob_service = BlobService(account_name=azureAccount, account_key=azureAccountKey)

	blob_service.put_block_blob_from_bytes(
	    azureContainer,
	    'precios.pickle',
	    pickle.dumps(data),
	    content_encoding='application/octet-stream'
	)

