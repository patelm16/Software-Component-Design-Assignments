JFLAGS = -g
JCLASS = -cp $(CLASSPATH):.:/usr/share/java/junit4.jar
JC = javac
JVM = java
CLASSES = src/*.java
MAIN = TestPathCalculation

default:
	$(JC) $(JFLAGS) $(JCLASS) $(CLASSES)

test: default

	cd src && $(JVM) $(JCLASS) org.junit.runner.JUnitCore $(MAIN)

doc:
	mkdir javadoc
	javadoc -sourcepath $(CLASSES) -d javadoc

clean:
	cd src && $(RM) *.class