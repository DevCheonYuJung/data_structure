package dataStructure;

public class Stack {
	
	public static void main(String[] args) {
		
		java.util.Stack<Integer> stack = new java.util.Stack<Integer>();
		
		System.out.println("Stack created : ");
		
		for(int i=0; i<10; i++) 
		stack.push(new Integer(i)); //0~9의 수로 스택을 구성한다.
		
		System.out.println("1pop : " + stack.pop()); //스택의 값을 뺀다
		System.out.println("2pop : " + stack.pop()); //스택의 값을 뺀다
		System.out.println("3pop : " + stack.pop()); //스택의 값을 뺀다
		System.out.println("4pop : " + stack.pop()); //스택의 값을 뺀다
	}

}
