/**
 * @author Meet Patel, patelm16
 *
 */
public class PointT {

	private double xcrd;
	private double ycrd;

	public PointT(double x, double y) throws InvalidPointException {
		if (x < 0 || x > Constants.MAX_X || y < 0 || y > Constants.MAX_Y)
			throw new InvalidPointException("Point is out of bounds.");
		xcrd = x;
		ycrd = y;
	}

	public double xcrd() {
		return xcrd;
	}

	public double ycrd() {
		return ycrd;
	}

	public double dist(PointT p) {
		return Math.sqrt(Math.pow((xcrd - p.xcrd), 2) + Math.pow((ycrd - p.ycrd), 2));
	}
}
