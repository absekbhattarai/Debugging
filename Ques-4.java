public class Stack {
    private Object[] elements;
    private int size = 0;
    private static final int DEFAULT_INITIAL_CAPACITY = 16;
    
    public Stack() {
    elements = new Object[DEFAULT_INITIAL_CAPACITY];
    }
    
    public void push(Object e) {
    ensureCapacity();
    elements[size++] = e;
    }
    
    public Object pop() {
    if (size == 0)
    throw new EmptyStackException();
    return elements[--size];
    }
    
    private void ensureCapacity() {
    if (elements.length == size)
    elements = Arrays.copyOf(elements, size + 8); //There was a memory leak problem. 
    //Everytime when elements.length equals to size; it multiplies which would take more memory space.
    //So we should add certain number say : 8 or 10 to the size. This would fix the problem.  
    }
    }
   