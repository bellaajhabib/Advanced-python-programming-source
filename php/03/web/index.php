<?php

declare(strict_types=1);

/** A dog object stores its own state and exposes behavior through methods. */
final class Dog
{
    public function __construct(public string $name, public int $age)
    {
    }

    public function bark(): string
    {
        return "{$this->name} says woof!";
    }

    public function birthday(): void
    {
        $this->age++;
    }
}

session_start();
if (!isset($_SESSION['dogs'])) {
    $_SESSION['dogs'] = [new Dog('Buddy', 2), new Dog('Luna', 4)];
}
$dogs = &$_SESSION['dogs'];
$message = '';
$error = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $action = (string) ($_POST['action'] ?? '');
    if ($action === 'add') {
        $name = trim((string) ($_POST['name'] ?? ''));
        $ageText = (string) ($_POST['age'] ?? '');
        $age = filter_var($ageText, FILTER_VALIDATE_INT);
        if ($name === '' || $age === false || $age < 0) {
            $error = 'Enter a name and a whole-number age of 0 or greater.';
        } else {
            $dogs[] = new Dog($name, $age);
            $message = "Created a new Dog object for {$name}.";
        }
    } elseif (in_array($action, ['bark', 'birthday'], true)) {
        $index = filter_var($_POST['index'] ?? null, FILTER_VALIDATE_INT);
        if ($index !== false && $index >= 0 && isset($dogs[$index])) {
            if ($action === 'bark') {
                $message = $dogs[$index]->bark();
            } else {
                $dogs[$index]->birthday();
                $message = "Happy birthday, {$dogs[$index]->name}! Age is now {$dogs[$index]->age}.";
            }
        } else {
            $error = 'That dog could not be found.';
        }
    }
}

function escape(string $value): string
{
    return htmlspecialchars($value, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
}
?>
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>OOP Dogs — PHP Web</title>
  <style>
    *{box-sizing:border-box}body{margin:0;background:#f4f6f1;color:#18251f;font:15px system-ui,sans-serif}.page{width:min(760px,calc(100% - 32px));margin:auto;padding:44px 0}.eyebrow{color:#397b57;font-size:.75rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase}h1,h2{letter-spacing:-.04em}h1{font-size:clamp(2.4rem,7vw,4rem);margin:8px 0}.intro,.status,footer{color:#65736a}.panel{background:white;border:1px solid #e0e7df;border-radius:16px;padding:18px;margin:12px 0}.create{display:flex;align-items:end;gap:10px;flex-wrap:wrap}.create h2{flex-basis:100%;margin:0}.field{display:grid;gap:5px;color:#65736a;font-size:.85rem;flex:1 1 150px}input{width:100%;padding:10px;border:1px solid #d9e1d9;border-radius:8px;font:inherit}button{border:0;border-radius:8px;padding:10px 14px;background:#236b43;color:white;font-weight:600;cursor:pointer}.secondary{background:#eef4ee;color:#236b43}.dog{display:flex;justify-content:space-between;align-items:center;gap:12px}.dog h2{margin:0 0 5px}.dog p{margin:0;color:#65736a}.icon{float:left;font-size:1.7rem;margin-right:12px}.actions{display:flex;gap:8px}.message{font-weight:600;color:#236b43}.error{padding:12px;border-radius:10px;background:#fff0ed;color:#963c30}footer{font-size:.84rem;margin-top:24px}@media(max-width:520px){.dog{align-items:flex-start;flex-direction:column}}
  </style>
</head>
<body><main class="page">
  <p class="eyebrow">PHP · Object-oriented programming</p>
  <h1>Dog playground</h1>
  <p class="intro">Each card represents a Dog object with its own state and methods.</p>
  <?php if ($error !== ''): ?><p class="error" role="alert"><?= escape($error) ?></p><?php endif; ?>
  <?php if ($message !== ''): ?><p class="message" role="status"><?= escape($message) ?></p><?php endif; ?>
  <form class="panel create" method="post">
    <h2>Create a Dog object</h2>
    <input type="hidden" name="action" value="add">
    <label class="field">Name <input name="name" required maxlength="40" placeholder="e.g. Max"></label>
    <label class="field">Age <input name="age" type="number" min="0" step="1" required placeholder="3"></label>
    <button>Add dog</button>
  </form>
  <section aria-label="Dog objects">
    <?php foreach ($dogs as $index => $dog): ?>
      <article class="panel dog">
        <div><span class="icon" aria-hidden="true">🐕</span><h2><?= escape($dog->name) ?></h2><p>Age: <strong><?= $dog->age ?></strong></p></div>
        <div class="actions">
          <form method="post"><input type="hidden" name="action" value="bark"><input type="hidden" name="index" value="<?= $index ?>"><button class="secondary">Bark</button></form>
          <form method="post"><input type="hidden" name="action" value="birthday"><input type="hidden" name="index" value="<?= $index ?>"><button class="secondary">Birthday (+1)</button></form>
        </div>
      </article>
    <?php endforeach; ?>
  </section>
  <footer>Lesson: methods act on the selected Dog object; birthdays change that object's age.</footer>
</main></body>
</html>
