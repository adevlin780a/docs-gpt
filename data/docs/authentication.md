# Authentication

To use the DocsGPT API, you must authenticate each request using an API key.

## Obtaining an API Key
1. Create an account on the DocsGPT Developer Portal.
2. Navigate to **Settings → API Keys**.
3. Click **Generate New Key** and copy your key safely.

## Using the API Key

You must include your key in the `Authorization` header of every request:
```bash
curl -X GET "https://api.docsgpt.dev/status" \
     -H "Authorization: Bearer YOUR_API_KEY"
