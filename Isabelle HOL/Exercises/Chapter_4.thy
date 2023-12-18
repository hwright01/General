theory Chapter_4
imports Main
begin

(*misc*)

lemma cantor_1 :  "\<not> surj(f :: 'a \<Rightarrow> 'a set)"
proof
  assume 0: "surj f"
  from 0 have 1: "\<forall>A. \<exists>a. A = f a" by (simp add: surj_def)
  from 1 have 2: "\<exists>a. f a = {x. x \<notin> f x}" by blast
  from 2 show "False" by blast
qed

lemma cantor_2 : "\<not> surj(f :: 'a \<Rightarrow> 'a set)"
proof
  assume "surj f"
  from this have "\<exists>a. f a = {x. x \<notin> f x}" by blast
  from this show "False" by blast
qed

inductive ev :: "nat \<Rightarrow> bool" where
ev0: "ev 0" |
evSS: "ev n \<Longrightarrow> ev(Suc(Suc n))"

fun evn :: "nat \<Rightarrow> bool" where
"evn 0 = True" |
"evn (Suc 0) = False" |
"evn (Suc(Suc n)) = evn n"

(*4.1*)

lemma assumes T: "\<forall> x y. T x y \<or> T y x"
  and A: "\<forall> x y. A x y \<and> A y x \<longrightarrow> x = y"
  and TA: "\<forall> x y. T x y \<longrightarrow> A x y" and "A x y"
shows "T x y"
proof -
  show "T x y" using assms by blast
qed

(*4.2*)

lemma "\<exists>ys zs. xs = ys @ zs \<and> (length ys = length zs \<or> length ys = length zs + 1)"
proof -
  consider (odd) "odd (length xs)" | (even) "even (length xs)" by auto
  then show ?thesis
  proof cases
    case odd
    let ?l1 = "take ((length xs + 1) div 2) xs"
    let ?l2 = "drop ((length xs + 1) div 2) xs"
    have "xs = ?l1 @ ?l2" by auto
    moreover have "length ?l1 = length ?l2 + 1"
      by (smt (verit, ccfv_threshold) add.commute add_diff_cancel_right' calculation left_add_twice length_append length_drop odd odd_succ_div_two odd_two_times_div_two_succ)
    thus ?thesis by blast
  next
    case even
    let ?l1 = "take ((length xs) div 2) xs"
    let ?l2 = "drop ((length xs) div 2) xs"
    have "xs = ?l1 @ ?l2" by auto
    moreover have "length ?l1 = length ?l2" using even by auto
    thus ?thesis by blast
  qed
qed

lemma "ev n \<Longrightarrow> ev (n-2)"
proof -
  assume "ev n"
  from this have "ev(n-2)"
  proof cases
    case ev0
    then show ?thesis by (simp add: ev.ev0)
  next
    case (evSS n)
    then show ?thesis by (simp add: ev.evSS)
  qed
  thus ?thesis by auto
qed

lemma "\<not> ev (Suc(Suc(Suc 0)))"
proof
  assume "ev (Suc(Suc(Suc 0)))" then show False
  proof cases
    assume "ev (Suc 0)" then show False by cases
  qed
qed