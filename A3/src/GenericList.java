/**
 * @author Meet Patel, patelm16
 *
 */

import java.util.ArrayList;

public class GenericList<T> {

	public static final int MAX_SIZE = 100;

	private ArrayList<T> s;

	public GenericList() {
		s = new ArrayList();
	}

	public void add(int i, T p) throws FullSequenceException, InvalidPositionException {
		if (s.size() == MAX_SIZE)
			throw new FullSequenceException("List is at max size. Cannot add to list.");
		if (i < 0 || i > s.size())
			throw new InvalidPositionException("Invalid position chosen.");
		s.add(i, p);
	}
	
	public void del(int i) throws InvalidPositionException{
		if(i < 0 || i > s.size() -1)
			throw new InvalidPositionException("Invalid position chosen.");
		s.remove(i);
	}
	
	public void setval (int i, T p) throws InvalidPositionException{
		if(i < 0 || i > s.size() -1)
			throw new InvalidPositionException("Invalid position chosen.");
		s.set(i, p);
	}
	
	public T getval (int i) throws InvalidPositionException{
		if(i < 0 || i > s.size() -1)
			throw new InvalidPositionException("Invalid position chosen.");
		return s.get(i);
	}
	
	public int size(){
		return s.size();
	}
}
