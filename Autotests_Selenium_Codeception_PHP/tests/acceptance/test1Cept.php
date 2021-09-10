<?php 
// php codecept.phar run acceptance _archive\TestGoogleSearchCept --html "result-test.html" --steps

use PHPUnit\Framework\Assert;

$I = new AcceptanceTester($scenario);
$I->wantTo('Test Google search');
$I->amOnUrl('https://www.google.com/');
$I->submitForm('//form', [
    'q' => 'GeForce 1650'
]);
$I->seeInTitle('GeForce 1650 - Поиск в Google');

$list = $I->grabMultiple('//div[@id="rso"]//h3');

Assert::assertNotEquals(0, count($list));
Assert::assertEquals('Игровая видеокарта GeForce GTX 1650 | NVIDIA', $list[0]);