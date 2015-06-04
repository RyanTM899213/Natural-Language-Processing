import java.util.Random;

/* Please note that below I am testing the insertion and search times for an array
 * and a Binary Search Tree in order to show the time differences of two structures.
 * This same concept would apply if we were using these two data structures to hold
 * a lexicon. Except here, I use only 1000 values at most. Usually, lexicons are tens
 * of thousands of entries long. Feel free to change the value of size below to see 
 * the time differences between the two structures and their operations.
 */

public class Tester {

    public static void main(String[] args) {
    
        Random rand = new Random();
        int size = 1000;  // test with 10, 100 and 1000 elements
        String[] arr = new String[size]; 
        BST<Integer, String> st = new BST<Integer, String>();
        long elapsed = 0;
        
        for (int i = 0; i < size/100; i++) {  // time how long it takes to populate
            long start = System.nanoTime();
            st.put(i, Integer.toString(i));  // key i, value i
            long end = System.nanoTime();
            elapsed += (end - start);        
        }
        System.out.println("> elapsed time to populate BST of size " + size/100 + " : " + elapsed);
        
        elapsed = 0;
        for (int i = 0; i < size/100; i++) {  // time how long it takes to populate
            long start = System.nanoTime();
            arr[i] = Integer.toString(i);  // key i, value i
            long end = System.nanoTime();
            elapsed += (end - start);        
        }
        System.out.println("> elapsed time to populate array of size " + size/100 + " : " + elapsed);
        
        //  ........................................ //    
        
        for (int i = 0; i < size; i++) {  // time how long it takes to populate
            long start = System.nanoTime();
            st.put(i, Integer.toString(i));  // key i, value i
            long end = System.nanoTime();
            elapsed += (end - start);        
        }
        System.out.println("> elapsed time to populate BST of size " + size + " : " + elapsed);
        
        elapsed = 0;
        for (int i = 0; i < size; i++) {  // time how long it takes to populate
            long start = System.nanoTime();
            arr[i] = Integer.toString(i);  // key i, value i
            long end = System.nanoTime();
            elapsed += (end - start);        
        }
        System.out.println("> elapsed time to populate array of size " + size + " : " + elapsed);
        
        // ........................................ //
        System.out.println(" notice that the times to populate array is faster than the BST\n");
        System.out.println(" ------ now let's test search times: -------");
        System.out.println("using pseudo random times to test search");
        elapsed = 0;
        for (int i = 0; i < size; i++) {  // this time is on average!
            String s = Integer.toString(rand.nextInt(size));
            long start = System.nanoTime();
            for (int j = 0; j < size; j++) {
                if (s == arr[j]) break;
            }
            long end = System.nanoTime();
            elapsed += (end - start);
        }
        System.out.println("> time to find random elements with array: " + elapsed);
        
        elapsed = 0;
        for (int i = 0; i < size; i++) {  // this time is on average!
            int s = rand.nextInt(size);
            long start = System.nanoTime();
            st.get(s);
            long end = System.nanoTime();
            elapsed += (end - start);
        }
        System.out.println("> time to find random elements with BST: " + elapsed);
        System.out.println("As we can see, the times for the BST operations should be faster\nthan the array operations");
        System.out.println("Therefore, the tree structure would be ideal to use with a lexicon");
        System.out.println("As we get larger and larger amounts of data to store using each structure,\nwe see a divergence in operation time");
    }
}    




