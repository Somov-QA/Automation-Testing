package tests.acceptance;

import org.testng.Assert;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;
import support.Helper.Selenium;
import support.StepsObject.GoogleSteps;

public class TestSampleTestNG {
    @BeforeTest
    public static void setup() {
        Selenium.initWebDriver();
        Selenium.browserFullScreen();
    }

    @Test
    public void testSearch() {
        GoogleSteps tester = new GoogleSteps(Selenium.driver);
        tester.driver.get("https://www.google.com/");
        tester.setValueInSearch("GeForce 1650");
        int result = tester.getCountResultSearch();
        Assert.assertNotEquals(0, result);
        System.out.println("Tests finished: SUCCESS");
    }

    @AfterTest
    public static void tearDown() {
        Selenium.quitWebDriver();
    }
}
