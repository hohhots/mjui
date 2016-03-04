module.exports = function(grunt) {
    
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-jshint');
    
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
        
        watch: {
            options: { livereload: true }, // reloads browser on save
            scripts: {
                files: ['src/app/js/**/*.js'],
                tasks: ['jshint']
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