theory Chapter_3
imports Main
begin

datatype 'a tree = Tip | Node "'a tree" 'a "'a tree"

(*3.1*)

fun set :: "'a tree \<Rightarrow> 'a set" where
"set Tip = {}"|
"set (Node l a r) = {a} Un (set l) Un (set r)"

fun leq_tree :: "int tree \<Rightarrow> int \<Rightarrow> bool" where
"leq_tree Tip x = True"|
"leq_tree (Node l a r) x = ((a \<le> x) & (leq_tree l x) & (leq_tree r x))"

fun ge_tree :: "int tree \<Rightarrow> int \<Rightarrow> bool" where
"ge_tree Tip x = True"|
"ge_tree (Node l a r) x = ((a > x) & (ge_tree l x) & (ge_tree r x))"

fun ord :: "int tree \<Rightarrow> bool" where
"ord Tip = True"|
"ord (Node l a r) = ((leq_tree l a) & (ord l) & (ge_tree r a) & (ord r))"

fun ins :: "int \<Rightarrow> int tree \<Rightarrow> int tree" where
"ins x Tip = (Node Tip x Tip)"|
"ins x (Node l a r) = (if (x = a) then (Node l a r) else (if (x \<le> a) then (Node (ins x l) a r) else (Node l a (ins x r))))"

lemma ins_correct_1: "set (ins x t) = {x} Un set t"
  by (induction t) auto

lemma ins_leq: "leq_tree t x1 \<longrightarrow> x2 \<le> x1 \<longrightarrow> leq_tree (ins x2 t) x1"
  by (induction t) auto

lemma ins_ge: "ge_tree t x1 \<longrightarrow> x2 > x1 \<longrightarrow> ge_tree (ins x2 t) x1"
  by (induction t) auto

lemma ins_correct_2: "ord t \<longrightarrow> ord (ins i t)"
  apply(induction t)
  by (auto simp add: ins_leq ins_ge)

  