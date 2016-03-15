module.exports = function(grunt) {
    
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-jshint');
    grunt.loadNpmTasks('intern');
    
    grunt.initConfig({
        //pkg: grunt.file.readJSON('package.json')
        
        jshint: {
            options: {
                curly: true
            },
            dev: {        
                src: ['src/app/js/**/*.js']
            }
        },
        
        intern: {
            someReleaseTarget: {
                options: {
                    runType: 'runner', // defaults to 'client'
                    config: 'tests/intern',
                    reporters: [ 'Console' ] //, 'Lcov' ],
                    //suites: [ 'tests/unit/all' ]
                }
            },
        },
        
        watch: {
            options: { livereload: true }, // reloads browser on save
            scripts: {
                files: ['src/app/js/**/*.js', 
                        'tests/**/*.js' 
                       ],
                tasks: ['jshint', 'intern']
            } //scripts
            // html: {
            //    files: ['src/app/*.html'],
            //    tasks: ['htmlhint:build']
            //}, //html
            //sass: {
            //    files: ['src/app/js/**/*.scss'],
            //    tasks: ['compass:dev', 'autoprefixer:build', 'cssc:build', 'cssmin:build']
            //}  //sass
        } //watch
    });

    // task setup 
    grunt.registerTask('default', ['watch']);
};