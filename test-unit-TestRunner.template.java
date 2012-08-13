package x.y.z;

import com.xtremelabs.robolectric.RobolectricTestRunner;
import org.junit.runners.model.InitializationError;

public class TestRunner extends RobolectricTestRunner {
    public TestRunner(Class testClass) throws InitializationError {
        super(testClass);
    }
}
