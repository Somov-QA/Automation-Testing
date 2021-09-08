const assert = require('assert');

describe('a test suite', async () => {    // необходим для вывода отчета
    it('a test case', async () => {       // тест кейс
        // Действия
        await browser.url('https://www.google.com/');
        let searchField = await $('//input[@name="q"]');
        await searchField.addValue('GeForce 1650');
        await browser.pause(3000);
        await browser.keys(['Return']);
        await browser.pause(5000);
       
        // Проверка заголовка страницы
        const title = await browser.getTitle();
        console.log('TEST TITLE:', title);
        assert.strictEqual(title, 'GeForce 1650 - Поиск в Google');

        // Проверка полученного результата поиска
        let list = await $('//div[@id="rso"]');
        console.log('FIRST SEARCH RESULT:', await list.$$('//div[@class="g"]')[0].getText('//h3'));

        let listElements = await $('//div[@id="rso"]').$$('//div[@class="g"]');
        console.log('LIST COUNT', await listElements.length);
        assert.notStrictEqual(await listElements.length , undefined);
        assert.notStrictEqual(await listElements.length , 0);
    });
});