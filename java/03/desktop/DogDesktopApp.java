import java.awt.BorderLayout;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.util.ArrayList;
import java.util.List;
import javax.swing.BorderFactory;
import javax.swing.DefaultListModel;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextField;
import javax.swing.ListSelectionModel;
import javax.swing.SwingUtilities;

/** Swing desktop app that makes the Java Dog OOP lesson interactive. */
public final class DogDesktopApp extends JFrame {
    private static final class Dog {
        private final String name;
        private int age;

        private Dog(String name, int age) {
            this.name = name;
            this.age = age;
        }

        private String bark() {
            return name + " says woof!";
        }

        private void birthday() {
            age++;
        }

        @Override
        public String toString() {
            return name + " — age " + age;
        }
    }

    private final List<Dog> dogs = new ArrayList<>(List.of(new Dog("Buddy", 2), new Dog("Luna", 4)));
    private final DefaultListModel<Dog> model = new DefaultListModel<>();
    private final JList<Dog> dogList = new JList<>(model);
    private final JTextField nameField = new JTextField(14);
    private final JTextField ageField = new JTextField(5);
    private final JLabel status = new JLabel("Choose a dog or create one.");

    private DogDesktopApp() {
        super("OOP Dogs — Java Desktop");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(560, 430);
        setLocationRelativeTo(null);

        JPanel content = new JPanel(new BorderLayout(10, 10));
        content.setBorder(BorderFactory.createEmptyBorder(18, 18, 18, 18));
        setContentPane(content);

        JPanel top = new JPanel(new BorderLayout(4, 4));
        top.add(new JLabel("Dog OOP playground — each row is a separate Dog object"), BorderLayout.NORTH);
        JPanel form = new JPanel(new FlowLayout(FlowLayout.LEFT));
        form.add(new JLabel("Name"));
        form.add(nameField);
        form.add(new JLabel("Age"));
        form.add(ageField);
        JButton add = new JButton("Add dog");
        add.addActionListener(event -> addDog());
        form.add(add);
        top.add(form, BorderLayout.CENTER);
        content.add(top, BorderLayout.NORTH);

        dogList.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        content.add(new JScrollPane(dogList), BorderLayout.CENTER);

        JPanel bottom = new JPanel(new BorderLayout(4, 8));
        JPanel actions = new JPanel(new FlowLayout(FlowLayout.LEFT));
        JButton bark = new JButton("Bark");
        bark.addActionListener(event -> bark());
        JButton birthday = new JButton("Birthday (+1)");
        birthday.addActionListener(event -> birthday());
        actions.add(bark);
        actions.add(birthday);
        bottom.add(actions, BorderLayout.NORTH);
        bottom.add(status, BorderLayout.SOUTH);
        content.add(bottom, BorderLayout.SOUTH);

        refresh(0);
    }

    private void addDog() {
        String name = nameField.getText().trim();
        int age;
        try {
            age = Integer.parseInt(ageField.getText().trim());
            if (age < 0 || name.isEmpty()) throw new NumberFormatException();
        } catch (NumberFormatException exception) {
            JOptionPane.showMessageDialog(this, "Enter a name and a whole-number age of 0 or more.", "Invalid dog", JOptionPane.ERROR_MESSAGE);
            return;
        }
        dogs.add(new Dog(name, age));
        nameField.setText("");
        ageField.setText("");
        refresh(dogs.size() - 1);
        status.setText("Created a new Dog object for " + name + ".");
    }

    private void bark() {
        Dog dog = dogList.getSelectedValue();
        if (dog != null) status.setText(dog.bark());
    }

    private void birthday() {
        int index = dogList.getSelectedIndex();
        if (index >= 0) {
            Dog dog = dogs.get(index);
            dog.birthday();
            refresh(index);
            status.setText("Happy birthday, " + dog.name + "! Age is now " + dog.age + ".");
        }
    }

    private void refresh(int selected) {
        model.clear();
        for (Dog dog : dogs) model.addElement(dog);
        if (!dogs.isEmpty()) dogList.setSelectedIndex(Math.max(0, Math.min(selected, dogs.size() - 1)));
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new DogDesktopApp().setVisible(true));
    }
}
