import java.util.*;

public class accenture {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt(sc.nextLine());
        HashMap<Integer, HashMap<String, String>> assigns = new HashMap<>();
        TreeMap<Integer, ArrayList<String>> prints = new TreeMap<>(Collections.reverseOrder());

        int depth = 0;
        for (int i = 0; i < n; i++) {
            String s = sc.nextLine();
            if (s.equals("{"))
                depth++;
            else if (s.equals("}"))
                depth--;
            else if (s.startsWith("assign")) {
                String[] ss = s.split(" ");

                HashMap<String, String> temp = assigns.getOrDefault(depth, new HashMap<String, String>());
                temp.put(ss[1], ss[2]);
                assigns.put(depth, temp);
            } else {
                String[] ss = s.split(" ");

                ArrayList<String> temp = prints.getOrDefault(depth, new ArrayList<String>());
                temp.add(ss[1]);
                prints.put(depth, temp);
            }
        }

        System.out.println(assigns);
        System.out.println(prints);

        for (Map.Entry<Integer, ArrayList<String>> e : prints.entrySet()) {
            int d = e.getKey();

            for (String l : e.getValue()) {
                int flag = 0;
                while (d >= 0) {
                    if (assigns.get(d) != null && assigns.get(d).keySet().contains(l)) {
                        flag = 1;
                        System.out.println(assigns.get(d).get(l));
                        break;
                    }
                    d--;
                }
                if (flag == 0)
                    System.out.println("undefined");
            }
        }
    }
}