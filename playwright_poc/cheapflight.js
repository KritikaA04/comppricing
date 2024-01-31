const playwright = require('playwright');
const cheerio = require('cheerio')
// let obj={}
// let arr=[]
 
async function test(){
    const browser = await playwright.chromium.launch({headless: false});
    
    const page = await browser.newPage();
    await page.goto('https://www.in.cheapflights.com/flight-search/BOM-DXB/2024-02-08?sort=bestflight_a');
    // let html = await page.content();
    
    // const $ = cheerio.load(html);
    await page.waitForTimeout(10000);
    //  obj["price"]=$('c-price-display u-text-ellipsis').text().trim()
    //  arr.push(obj)
    //  console.log(arr)
    // const divprice = $('.c-price-display u-text-ellipsis')
    // divprice.each((i,div) => {
    //     console.log($(div).text());
    // })
    const pricing= page.locator('[class= "f8F1-price-text"]');
    const text = await pricing.allTextContents();
    console.log(text);
    await browser.close();
}
 
test()