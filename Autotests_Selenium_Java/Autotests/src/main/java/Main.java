import org.junit.internal.TextListener;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import tests.TestSampleJUnit;

import org.testng.TestNG;
import support.Helper.ListenerTestNG;
import tests.TestSampleTestNG;

public class Main {

    public static void main(String[] args){
        /*
        Result result = JUnitCore.runClasses(TestSampleJUnit.class);
        JUnitCore junit = new JUnitCore();
        junit.addListener(new TextListener(System.out));
        junit.run(TestSampleJUnit.class);
         */

        TestNG test = new TestNG();
        test.setTestClasses(new Class[]{
            TestSampleTestNG.class
        });
        test.addListener(new ListenerTestNG());
        test.setDefaultSuiteName("TestSampleTestNG");
        test.setOutputDirectory("/out");
        test.run();
    }
}
