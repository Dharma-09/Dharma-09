<h2> 👋 Hi, I'm Dharma</h2>

[![Twitter: im_dharma09](https://img.shields.io/twitter/follow/im_dharma09?style=flat-square)](https://twitter.com/im_dharma09)
![Hi👋](https://komarev.com/ghpvc/?username=Dharma-09&abbreviated=true)

## ✨ My Recent Activity

**Open Source Contribution**

1. 🎉 Merged PR [#8122](https://github.com/wagtail/wagtail/pull/8122) in [wagtail/wagtail](https://github.com/wagtail/wagtail)
2. 🎉 Merged PR [#6859](https://github.com/kubernetes/autoscaler/pull/6859) in [kubernetes/autoscaler/](https://github.com/kubernetes/autoscaler/)
3. 🎉 Merged PR [#1872](https://github.com/kolide/launcher/pull/1872) in [Kolide/launcher](https://github.com/kolide/)
4. 📫 Closed PR [#13310](https://github.com/kubevirt/kubevirt/pull/13310) in [KubeVirt/kubevirt](https://github.com/kubevirt/kubevirt)
5. 🎉 Merged PR [#7170](https://github.com/prometheus-operator/prometheus-operator/pull/7170) & [#7241](https://github.com/prometheus-operator/prometheus-operator/pull/7241) & [#7247](https://github.com/prometheus-operator/prometheus-operator/pull/7247) & [#7966](https://github.com/prometheus-operator/prometheus-operator/pull/7966) in [prometheus-operator/prometheus-operator](https://github.com/prometheus-operator/prometheus-operator)
6. 🎉 Merged PR [#31303](https://github.com/backstage/backstage/pull/31303) & [#6033](https://github.com/backstage/community-plugins/pull/6033) in [Backstage/backstage](https://github.com/backstage/backstage)
7. 🎉 Merged PR [#10173](https://github.com/aquasecurity/trivy/pull/10173) & [#10215](https://github.com/aquasecurity/trivy/pull/10215) & [#10187](https://github.com/aquasecurity/trivy/pull/10187) in [Aquasecurity/trivy](https://github.com/aquasecurity/trivy)

---

```go
package main

import "fmt"

type Me struct {
	Pseudonym            string
	Code                 string
	BestAndFavoriteSkill string
	Certifications       []string
}

func (m *Me) PrintInfo() {
	fmt.Println("Pseudonym: ", m.Pseudonym)
	fmt.Println("Code: ", m.Code)
	fmt.Println("Best and Favorite Skill: ", m.BestAndFavoriteSkill)
	fmt.Println("Certifications: ")
	for _, cert := range m.Certifications {
		fmt.Println("Azure - 104", cert)
	}
}

func main() {
	me := &Me{
		Pseudonym:            "Dharma",
		Code:                 "GoLang, Javascript and Python",
		BestAndFavoriteSkill: "Design secure cloud architectures, harden DevOps pipelines :D",
		Certifications:       []string{ "Azure-104"},
	}
	me.PrintInfo()
} //To run this code go run file_n.go
```

