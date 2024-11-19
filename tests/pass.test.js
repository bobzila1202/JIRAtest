import { test, expect } from '@playwright/test';

 

test('passing test', async ({ page }) => {

 

  await page.goto('https://www.asn.com/', { waitUntil: 'load', timeout: 30000 });

 

  await page.waitForTimeout(5000);

});