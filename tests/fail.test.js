import { test, expect } from '@playwright/test';

 

test('failing test', async ({ page }) => {

  await page.goto('https://www.google.com/', { waitUntil: 'load', timeout: 30000 });

 

  await page.getByRole('button', { name: 'Reject all button does not exist' }).click();

 

  await page.getByLabel('Search', { exact: true }).click();

  await page.getByLabel('Search', { exact: true }).fill('alcatel submarine networks');

 

  await page.goto('https://www.google.com/search?q=alcatel+submarine+networks', { waitUntil: 'load', timeout: 30000 });

 

  await page.locator('#rso').getByRole('link', { name: 'Nonexistent Link' }).click();

 

  await page.waitForTimeout(5000);

});