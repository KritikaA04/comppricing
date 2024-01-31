const playwright = require('playwright');
const cheerio = require('cheerio');

async function main() {
    const browser = await playwright.chromium.launch({
        headless: false // setting this to true will not run the UI
    });

    let obj={}
    let arr=[]

    const page = await browser.newPage();
    await page.goto('https://www.makemytrip.com/flight/search?itinerary=BOM-DXB-08/02/2024&tripType=O&paxType=A-1_C-0_I-0&intl=true&cabinClass=E&ccde=IN&lang=eng');
    let html = await page.content();
    // const pageTitle = await page.title(); 
    // console.log(pageTitle);
    obj["price"]=$('div.textRight flexOne').text()
    arr.push(obj)
    console.log(arr)
    
    
    // // Wait for the element to be present in the DOM
    // const divSelector = '.blackText fontSize18 blackFont white-space-no-wrap clusterViewPrice'; // Replace 'your-div-class' with the actual class of the div you want to scrape
    // // const divSelector = '.textRight flexOne'; // Replace 'your-div-class' with the actual class of the div you want to scrape
    // await page.waitForSelector(divSelector, { visible: true });
    // // await page.waitForSelector('.textRight.flexOne', { visible: true });


    // // Use page.$ to select the element by its class
    // const divElementHandle = await page.$(divSelector);

    // // Extract the content or other information from the div
    // if (divElementHandle) {
    //     const divContent = await page.evaluate(div => div.textContent, divElementHandle);
    //     console.log('Content of the selected div:', divContent);
    // } else {
    //     console.log('Div not found with the specified class.');
    // }

    // // await page.waitForTimeout(5000); // wait for 5 seconds
    await browser.close();
}

main();


// const playwright = require('playwright');
// async function main() =>{
//     // for (const browserType of ['chromium', 'firefox',  'webkit'])
//     // {
//     //    const browser = await playwright[browserType].launch()
//         const browser = await playwright.chromium.launch();
//         const context = await browser.newContext()
//         const page = await context.newPage()
//         await page.goto("https://finance.yahoo.com/world-indices")
//         const pageTitle = await page.title(); 
//         console.log(pageTitle);
//         // await page.wait_for_timeout(10000)
//         await browser.close();
//     // }
// }
// main();