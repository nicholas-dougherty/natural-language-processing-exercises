[Notes](https://doc-08-4g-apps-viewer.googleusercontent.com/viewer/secure/pdf/1o76boig9ep360dibg2tl9umkoiusm99/utgptutd5f8j32rohml1b4uc6qn1tcs9/1651852200000/drive/16039635235969525294/ACFrOgCyf6uFaQl-4N3RFE8JzzKfSWOhRgxRvgrZ7OavC1VY6O3oo5TovJ5oyQdKXcmUjS5UDRAy6DpzgjERhV2jgu0P-T-UVa7U1OunC8Oq-DtKf21T5Thml4c30WC4fm0RgQLU7wGSHpbpfssA?print=true&nonce=cjpnt5gpnjj4e&user=16039635235969525294&hash=ogtmih03f77a6p963r11sa6jf6kl13aj) for Web Scraping.

Head: Meta Page Information. This effectively happens under the hood. 
Body: Page Contents. The parts of this are what are actually seen in the browser while visiting a website. 
Contained within the body are sub-bracketed (angle bracketed, or chevroned) Elements. 
The children of the tags are what lie within these via the tag namei.e. (<h1 class) These are the opening and closing tabs. 

HTML Document Anatomy

<!DOCTYPE html>
<html lang="en"> 
<head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Web Scraping Demo Pages</title>
      <link href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css" rel="stylesheet" />
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.4.1/font/bootstrap-icons.css" />
</head>
<body class="grid justify-center items-center h-screen">
      <div class="text-center space-y-16">
      <h1 class="text-4xl">Web Scraping Demo Pages</h1>
      <div class="grid grid-cols-2 text-2xl">
            <p><a class="text-blue-600 hover:underline" href="/people">People</a></p>
            <p><a class="text-blue-600 hover:underline" href="/news">News</a></p>
      </div>
      </div>
</body>
</html>


EXAMPLE.com

2. Identify the document head and document body.
3. How many elements are in the document body?
4. What element attributes do you see?

<!doctype html>
<html>
<head>
    <title>Example Domain</title>

    <meta charset="utf-8" />
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style type="text/css">
    body {
        background-color: #f0f0f2;
        margin: 0;
        padding: 0;
        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
        
    }
    div {
        width: 600px;
        margin: 5em auto;
        padding: 2em;
        background-color: #fdfdff;
        border-radius: 0.5em;
        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
    }
    a:link, a:visited {
        color: #38488f;
        text-decoration: none;
    }
    @media (max-width: 700px) {
        div {
            margin: 0 auto;
            width: auto;
        }
    }
    </style>    
</head>

<body>
<div>
    <h1>Example Domain</h1>
    <p>This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>
    <p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>