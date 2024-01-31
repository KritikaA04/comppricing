const playwright = require('playwright');
const cheerio = require('cheerio')
// let obj={}
// let arr=[]
 
async function test(){
    const browser = await playwright.chromium.launch({headless: false});
    
    const page = await browser.newPage();
    await page.goto('https://www.makemytrip.com/flight/search?itinerary=BOM-DXB-08/02/2024&tripType=O&paxType=A-1_C-0_I-0&intl=true&cabinClass=E&ccde=IN&lang=eng');
    let html = await page.content();
    
    const $ = cheerio.load(html);
    await page.waitForTimeout(10000);
    //  obj["price"]=$('div.blackText.fontSize18.blackFont.white-space-no-wrap.clusterViewPrice').text().trim()
    //  arr.push(obj)
    //  console.log(arr)
    const divprice = $('.blackText fontSize18 blackFont white-space-no-wrap clusterViewPrice')
    divprice.each((i,div) => {
        console.log($(div).text());
    })
    // const pricing= page.locator('[class= "blackText fontSize18 blackFont white-space-no-wrap clusterViewPrice"]');
    // const text = await pricing.allTextContents();
    // console.log(text);
    await browser.close();
}
 
test()