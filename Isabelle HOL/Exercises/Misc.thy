theory Misc
  imports Main "HOL-Library.Disjoint_Sets"
begin

fun sum :: "nat list \<Rightarrow> nat" where
"sum [] = 0"|
"sum (x # xs) = x + sum xs"

definition sumrep :: "nat \<Rightarrow> nat list \<Rightarrow> bool" where
"sumrep x xs \<equiv> sum xs = x"

definition filled_elts :: " nat set set \<Rightarrow> bool" where
"filled_elts X \<equiv> (\<forall> x \<in> X. card x = 1 + Max x - Min x)"

definition box_sum :: "nat \<Rightarrow> nat \<Rightarrow> nat set set set" where
"box_sum n s = {x \<in> Pow(Pow(lessThan (n::nat))). partition_on (lessThan (n::nat)) x \<and>
 filled_elts x \<and> card x = s}"

value "partition_on {(1::nat),2,3} {{1,2},{3}}"
value "Pow (atMost (3::nat))"
value "card {(1::nat),2,3}"
value "card (box_sum 3 2)"
value "box_sum 3 2"
value "{x \<in> box_sum 3 2. {2} \<in> x}"

lemma box_sum_finite:
  assumes "n>0 \<and> k>0"
  shows "finite (box_sum n k)"
proof -
  have "box_sum n k \<subseteq> Pow(Pow(lessThan n))"
  proof -
    have "\<forall>x\<in>box_sum n k. x\<in>Pow(Pow(lessThan n))"
      by (simp add: box_sum_def)
    then show ?thesis by blast
  qed
  then show ?thesis
    by (meson finite_Pow_iff finite_lessThan rev_finite_subset)
qed

lemma test2:
  assumes "n>0 \<and> k>0"
  shows "card (box_sum (Suc n) (Suc k)) = card {x \<in> box_sum (Suc n) (Suc k). {n} \<in> x} +
 card {x \<in> box_sum (Suc n) (Suc k). {n} \<notin> x}"
proof -
  have "box_sum (Suc n) (Suc k) = {x \<in> box_sum (Suc n) (Suc k). {n} \<in> x} \<union>
 {x \<in> box_sum (Suc n) (Suc k). {n} \<notin> x}"
  proof -
  have  "box_sum (Suc n) (Suc k) \<subseteq> {x \<in> box_sum (Suc n) (Suc k). {n} \<in> x} \<union>
 {x \<in> box_sum (Suc n) (Suc k). {n} \<notin> x}" by blast
  show ?thesis
    by blast
  qed
  moreover have "finite {x \<in> box_sum (Suc n) (Suc k). {n} \<in> x} \<and>
 finite {x \<in> box_sum (Suc n) (Suc k). {n} \<notin> x}" using box_sum_finite by auto
  finally show ?thesis using Finite_Set.card_Un_disjoint
    by (metis (no_types, lifting) \<open>finite {x \<in> box_sum (Suc n) (Suc k). {n} \<in> x} \<and> 
  finite {x \<in> box_sum (Suc n) (Suc k). {n} \<notin> x}\<close> 
  calculation disjoint_iff_not_equal mem_Collect_eq)
qed
  

(*
lemma two:
  assumes "n>0 \<and> k>0"
  shows "card (box_sum (Suc n) (Suc k)) = card (box_sum n k) + card (box_sum n (Suc k))"
proof -
  have box_sum (Suc n) (Suc k) = {x \<in> box_sum (Suc n) (Suc k). Suc n \<in> x}

lemma one: 
  assumes "n>0 \<and> k>0"
  shows "card (box_sum n k) = n-1 choose k-1"



definition sum2rep :: "nat list \<Rightarrow> (nat \<Rightarrow> nat list \<Rightarrow> bool)" where
"sum2rep xs = sumrep ((sum xs) xs)"

definition box_to_choice :: "nat set set \<Rightarrow> nat set" where
"

definition srset :: "nat \<Rightarrow> set \<Rightarrow> bool" where
"srset x S \<equiv> 
*)