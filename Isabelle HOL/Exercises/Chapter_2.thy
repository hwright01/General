theory Chapter_2
imports Main
begin

(*2.1*)
value "1 + (2::nat)"
value "1 + (2::int)"
value "1 - (2::nat)"
value "1 - (2::int)"

(*2.2*)
fun add :: "nat \<Rightarrow> nat \<Rightarrow> nat" where
"add 0 n = n" |
"add (Suc m) n = Suc(add m n)"

lemma add_assoc [simp] : "add (add p q) r  = add p (add q r)"
  apply(induction p)
   apply(auto)
  done

lemma add_02 [simp] : "add m 0 = m" apply(induction m)
apply(auto)
done

lemma add_plus1 [simp] : "Suc (add q p) = add q (Suc p)"
  apply(induction q)
   apply(auto)
  done

lemma add_comm [simp] : "add p q = add q p"
  apply(induction p)
   apply(auto)
  done

fun double :: "nat \<Rightarrow> nat" where
"double 0 = 0"|
"double (Suc(n)) = Suc(Suc(double(n)))"

lemma doublen [simp] : "double m = add m m"
  apply(induction m)
   apply(auto)
  done

(*2.3*)
fun count :: "'a \<Rightarrow> 'a list \<Rightarrow> nat" where
"count x [] = 0"|
"count x (t # xs) = (if x = t then 1 else 0) + (count x xs)"

lemma countconstraint: "count x xs \<le> length xs"
  apply(induction xs)
   apply(auto)
  done

(*2.4*)
fun snoc :: "'a list \<Rightarrow> 'a \<Rightarrow> 'a list" where
"snoc [] x = [x]"|
"snoc (t # xs) x = t # (snoc xs x)"

fun reverse :: "'a list \<Rightarrow> 'a list" where
"reverse [] = []"|
"reverse (x # xs) = snoc (reverse xs) x"

lemma reversnoc[simp]: "reverse (snoc xs a) = a # (reverse xs)"
  apply(induction xs)
   apply auto
  done

lemma reversym: "reverse (reverse xs) = xs"
  apply(induction xs)
  apply auto
  done

(*2.5*)
fun sum_upto :: "nat \<Rightarrow> nat" where
"sum_upto 0 = 0"|
"sum_upto (Suc(x)) = 1 + x + sum_upto(x)"

lemma sum_from: "sum_upto n = n * (n+1) div 2"
  apply(induction n)
   apply(auto)
  done      

(*2.6*)
datatype 'a tree = Tip | Node "'a tree" 'a "'a tree"

fun contents :: "'a tree \<Rightarrow> 'a list" where
"contents Tip = []"|
"contents (Node l a r) = (contents l) @ (a # contents r)"

fun sum_tree :: "nat tree \<Rightarrow> nat" where
"sum_tree Tip = 0"|
"sum_tree (Node l a r) = (sum_tree l) + a + (sum_tree r)"

lemma sum_equiv: "sum_tree t = sum_list (contents t)"
  apply (induction t)
   apply auto
  done

(*2.7*)

fun pre_order :: "'a tree \<Rightarrow> 'a list" where
"pre_order Tip = []"|
"pre_order (Node l a r) = (pre_order l) @ (a # (pre_order r))"

fun post_order :: "'a tree \<Rightarrow> 'a list" where
"post_order Tip = []"|
"post_order (Node l a r) = (pre_order r) @ (a # (pre_order l))"

fun mirror :: "'a tree \<Rightarrow> 'a tree" where
"mirror Tip = Tip"|
"mirror (Node l a r) = Node (mirror r)  a (mirror l)"

(*Not defined correctly but I don't care*)

(*2.8*)

fun intersperse :: "'a \<Rightarrow> 'a list \<Rightarrow> 'a list" where
"intersperse a [] = []"|
"intersperse a [x] = [x]"|
"intersperse a (x # xs) = x # (a # (intersperse a xs))"

lemma map_sperse: "map f (intersperse a xs) = intersperse (f a) (map f xs)"
  apply(induction a xs rule: intersperse.induct)
    apply(auto)
  done

(*2.9*)
fun itadd :: "nat \<Rightarrow> nat \<Rightarrow> nat" where
"itadd 0 n = n"|
"itadd (Suc 0) n = Suc n"|
"itadd (Suc m) n = itadd (Suc 0) (itadd m n)"

lemma add_1 : "Suc m = add m (Suc 0)"
  apply(induction m)
   apply(auto)
  done

lemma add_equiv: "itadd n m = add n m"
  apply(induction n m rule: itadd.induct)
    apply(auto)
  apply(rule add_1)
  done

(*2.10*)
datatype tree0 = Tip | Node "tree0" "tree0"

fun explode :: "nat \<Rightarrow> tree0 \<Rightarrow> tree0" where
"explode 0 t = t" |
"explode (Suc n) t = explode n (Node t t)"

fun nodes :: "tree0 \<Rightarrow> nat" where
"nodes Tip = 1"|
"nodes (Node l r) = nodes l + nodes r"

lemma explosion_count : "nodes (explode n t) = (nodes t) * 2^n"
  apply(induction n arbitrary: t)
   apply(auto)
  done

(*2.11*)
datatype exp = Var | Const int | Add exp exp | Mult exp exp

fun eval :: "exp \<Rightarrow> int \<Rightarrow> int" where
"eval Var x = x"|
"eval (Const n) x = n"|
"eval (Add a b) x = eval a x + eval b x"|
"eval (Mult a b) x = eval a x * eval b x"

fun evalp :: "int list \<Rightarrow> int \<Rightarrow> int" where
"evalp [] x = 0"|
"evalp (a # xs) x = a + x * evalp xs x"

fun ewadd :: "int list \<Rightarrow> int list \<Rightarrow> int list" where
"ewadd x [] = x"|
"ewadd [] x = x"|
"ewadd (x # xs) (y # ys) = (x+y) # ewadd xs ys"

fun constmul :: "int \<Rightarrow> int list \<Rightarrow> int list" where
"constmul n [] = []"|
"constmul n (x # xs) = n*x # (constmul n xs)"

(*
This was my initial attempt. It made it ver hard to prove lemma coeffs_mul.

fun ewmul :: "int list \<Rightarrow> int list \<Rightarrow> int list" where
"ewmul x [] = []"|
"ewmul [] y = []"|
"ewmul [x] [y] = [x*y]"|
"ewmul (x # xs) (y # ys) = x*y # ewadd (ewadd (constmul y xs) (constmul x ys)) (0 # ewmul xs ys)"
*)

fun ewmul :: "int list \<Rightarrow> int list \<Rightarrow> int list" where
"ewmul xs [] = []"|
"ewmul xs (y # ys) = ewadd (constmul y xs) (0 # (ewmul xs ys))"

fun coeffs :: "exp \<Rightarrow> int list" where
"coeffs Var = [0,1]"|
"coeffs (Const n) = [n]"|
"coeffs (Add a b) = ewadd (coeffs a) (coeffs b)"|
"coeffs (Mult a b) = ewmul (coeffs a) (coeffs b)"

lemma coeffs_const: "evalp (constmul y xs) x = y * evalp xs x"
  apply(induction xs)
   apply(auto simp add: algebra_simps)
  done

lemma coeffs_add: "evalp (ewadd e1 e2) x = evalp e1 x + evalp e2 x"
  apply(induction e1 e2 rule: ewadd.induct)
    apply(auto simp add: algebra_simps)
  done

lemma coeffs_mul: "evalp (ewmul e1 e2) x = evalp e1 x * evalp e2 x"
  apply(induction e1 e2 rule: ewmul.induct)
      apply(auto simp add: algebra_simps)
   apply(subst coeffs_add)
  apply(auto)
  apply(rule coeffs_const)
  done

lemma coeffs_preserves : "evalp (coeffs e) x = eval e x"
  apply(induction e)
     apply(auto simp add: algebra_simps)
   apply(subst coeffs_add)
   apply(simp)
  apply(subst coeffs_mul)
  apply(auto)
  done

end