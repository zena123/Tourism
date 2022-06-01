var appRegistration = new Vue({
    el: '#id-register-app',
    mixins: [djVueMixin],
    actionURL: '{% url "api:user_api:registration-list" %}',
    data() {
        return {
        form:{
            first_name:"",
            last_name:"",
            username:"",
            dob:"",
            interests:"",
            is_publisher:"",
        }
        }
    },
    methods: {
        submit() {
            // reset errors
            this.nonFieldErrors = []
            axios.post(this.actionURL, Object.assign({}, this.form, this.files))
                .then(this.success)
                .catch(this.error)
        },
        success(response) {
            console.log("success");
        },
        error(error, ref = "form") {
            if (error.response && error.response.status === 400) {
                let errors = error.response.data
                this.renderFieldErrors(errors, ref)
            } else {
                this.nonFieldErrors.push("Error! Contact an administrator.")
            }
        },
    },

})

let AppApplication = document.getElementById('application');
AppApplication.removeAttribute("hidden");