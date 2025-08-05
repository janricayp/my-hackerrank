import java.util.*;

public class SecondLowestScore {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt(); 
        scanner.nextLine(); 

        
        List<List<Object>> students = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            String name = scanner.nextLine();
            double score = Double.parseDouble(scanner.nextLine());

            List<Object> student = new ArrayList<>();
            student.add(name);
            student.add(score);

            students.add(student);
        }

        
        students.sort(Comparator.comparingDouble(s -> (double) s.get(1)));

       
        double lowest = (double) students.get(0).get(1);
        Double secondLowest = null;

        
        for (List<Object> student : students) {
            double score = (double) student.get(1);
            if (score > lowest) {
                secondLowest = score;
                break;
            }
        }

        
        List<String> names = new ArrayList<>();
        for (List<Object> student : students) {
            if (((double) student.get(1)) == secondLowest) {
                names.add((String) student.get(0));
            }
        }

        
        Collections.sort(names);

        
        for (String name : names) {
            System.out.println(name);
        }

        scanner.close();
    }
}
