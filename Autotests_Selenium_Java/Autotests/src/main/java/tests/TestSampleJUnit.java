package tests;

import org.junit.AfterClass;
import org.junit.Assert;
import org.junit.BeforeClass;
import org.junit.Test;
import support.Helper.Selenium;
import support.StepsObject.GoogleSteps;


public class TestSampleJUnit {
    @BeforeClass
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

    @AfterClass
    public static void tearDown() {
        Selenium.quitWebDriver();
    }
}

