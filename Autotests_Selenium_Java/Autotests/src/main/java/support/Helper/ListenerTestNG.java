package support.Helper;

import org.testng.ISuite;
import org.testng.ISuiteListener;

public class ListenerTestNG implements ISuiteListener {
    public void onStart(ISuite suite){
        System.out.println("directory = " + suite.getOutputDirectory());
    }

    public void onFinish(ISuite suite) {
        System.out.println("methods = " + suite.getAllMethods());
        System.out.println("results = " + suite.getResults());
    }
}
